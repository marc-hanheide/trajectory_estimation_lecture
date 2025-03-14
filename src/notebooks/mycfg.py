c = get_config()  #noqa


c.NbConvertApp.export_format = 'slides'
c.TemplateExporter.exclude_input = True
c.NbConvertApp.notebooks = [
    "introduction.ipynb",
    "kalman.ipynb"
]
c.SlidesExporter.reveal_theme = 'white'
c.SlidesExporter.reveal_scroll = True
c.SlidesExporter.reveal_number = 'c/t'
#c.SlidesExporter.reveal_height = '200'
