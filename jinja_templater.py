import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

class DocumentRenderer:
    def __init__(self, template_path, attributes, save_path):
        self.template_path = template_path
        self.attributes = attributes
        self.save_path = save_path
        self.template_dir, self.template_file = os.path.split(template_path)
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.template = None
        self.rendered_content = None

    def read(self):
        """Read the template document."""
        self.template = self.env.get_template(self.template_file)

    def render(self):
        """Render the document using the attributes."""
        if self.template is None:
            raise ValueError("Template document is not loaded. Call read() method first.")
        self.rendered_content = self.template.render(self.attributes)

    def save(self):
        """Save the rendered document with a timestamp."""
        if self.rendered_content is None:
            raise ValueError("Document is not rendered. Call render() method first.")
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        base, ext = os.path.splitext(self.save_path)
        final_save_path = f"{base}_{timestamp}{ext}"
        
        with open(final_save_path, 'w') as file:
            file.write(self.rendered_content)
        
        print(f"Document saved to {final_save_path}")


class DocumentRendererBuilder:
    def __init__(self):
        self._template_path = None
        self._attributes = {}
        self._save_path = None

    def set_template_path(self, template_path):
        self._template_path = template_path
        return self

    def set_attributes(self, attributes):
        self._attributes = attributes
        return self

    def set_save_path(self, save_path):
        self._save_path = save_path
        return self

    def build(self):
        if not self._template_path:
            raise ValueError("Template path must be provided.")
        if not self._save_path:
            raise ValueError("Save path must be provided.")
        return DocumentRenderer(self._template_path, self._attributes, self._save_path)


# Example usage:
attributes = {"name": "John Doe", "date": "2024-06-18"}
builder = DocumentRendererBuilder()
doc_renderer = (builder
                .set_template_path("template.txt")
                .set_attributes(attributes)
                .set_save_path("output.txt")
                .build())

doc_renderer.read()
doc_renderer.render()
doc_renderer.save()
