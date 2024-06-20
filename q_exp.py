from dataclasses import dataclass 
from functools import cached_property, lru_cache

class Warehouse:
    def __init__(self, df):
        self.df = df
        self.cache_dict = {}

    @cached_property
    def loss_df_grouped_by_uids (self):
        return df.group_by('UID').agg(pl.col('VALUE').sum().alias('TOTAL_VALUE'))
    
    @lru_cache(maxsize=128)
    def _get_VALUE_for_quantile(self, quantile):
        return self.loss_df_grouped_by_uids['TOTAL_VALUE'].quantile(quantile)
    
    def _get_UIDs_for_quantile (self, loss):
        return self.loss_df_grouped_by_uids.filter(pl.col('TOTAL_VALUE') == loss)['UID'][0]
    
    def _check_epsilon (self, center, epsilon):
        if epsilon < 0:
            raise ValueError("Epsilon must be greater than or equal to 0")
        if center+epsilon > 1:
            raise ValueError("Center + Epsilon must be less than or equal to 1")
        if center-epsilon < 0:
            raise ValueError("Center - Epsilon must be greater than or equal to 0")
        
    @lru_cache(maxsize=128)
    def get_VALUE_in_neighbourhood (self, center, epsilon):    
        self._check_epsilon(center, epsilon)    
        quantiles = [center-epsilon, center, center+epsilon]
        VALUE = [self._get_VALUE_for_quantile(q) for q in quantiles]
        UIDs = [self._get_UIDs_for_quantile(loss) for loss in VALUE]
        return pl.DataFrame({
            'QUANTILE': quantiles,
            'VALUE': VALUE,
            'UID': UIDs
        })
    
    def _get_filtered_df_by_UIDs(self, UIDs):
        return self.df.filter(pl.col('UID').is_in(UIDs))

    @lru_cache(maxsize=128)
    def average_VALUE_by_NAMES_in_neighbourhood(self, center, epsilon):
        neighbourhood = self.get_VALUE_in_neighbourhood(center, epsilon)
        UIDs = neighbourhood['UID'].to_list()
        filtered_df = self._get_filtered_df_by_UIDs(UIDs)
        self.cache_dict[(center, epsilon)] = {"UIDs": UIDs, "filtered_df": filtered_df}  
        return filtered_df.group_by('NAMES').agg(pl.col('VALUE').mean().alias('AVERAGE_VALUE'))
