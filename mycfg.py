c = get_config()  #noqa


c.NbConvertApp.export_format = 'slides'

c.TemplateExporter.exclude_input = False
c.NbConvertApp.notebooks = [
    "*.ipynb"
]
c.SlidesExporter.reveal_theme = 'white'
c.SlidesExporter.reveal_scroll = True
c.SlidesExporter.reveal_number = 'c/t'
#c.SlidesExporter.reveal_height = '800'
#c.SlidesExporter.reveal_height = '450'

c.SlidesExporter.extra_template_paths = ['./templates/']
c.SlidesExporter.extra_template_basedirs=["./templates/"]

c.TemplateExporter.template_name = 'marc_reveal'