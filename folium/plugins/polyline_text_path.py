# -*- coding: utf-8 -*-
"""
PolyLine Text Path
-----------

https://github.com/makinacorpus/Leaflet.TextPath

Shows a text along a PolyLine.

"""

from branca.element import Figure, JavascriptLink

from folium.features import MacroElement

from jinja2 import Template


class PolyLineTextPath(MacroElement):
    """Shows a text along a PolyLine."""
    def __init__(self, polyline, text, repeat=False, center=False, below=False,
                 offset=0, orientation=0, attributes=None):
        """Shows a text along a PolyLine.

        Parameters
        ----------
            polyline: folium.features.PolyLine object
                The folium.features.PolyLine object to attach the text to.

            text: string
                The string to be attached to the polyline.

            repeat: bool, default False
                Specifies if the text should be repeated along the polyline.

            center: bool, default False
                Centers the text according to the polyline's bounding box

            below: bool, default False
                Show text below the path

            offset: int, default 0
                Set an offset to position text relative to the polyline.

            orientation: int, default 0
                Rotate text to a specified angle.

            attributes: dictionary
                Object containing the attributes applied to the text tag.
                Check valid attributes here:
                    https://developer.mozilla.org/en-US/docs/Web/SVG/Element/text#Attributes
                Example: {'fill': '#007DEF', 'font-weight': 'bold', 'font-size': '24'}


        """
        super(PolyLineTextPath, self).__init__()
        self._name = 'PolyLineTextPath'
        self.polyline = polyline
        self.text = text
        self.repeat = bool(repeat)
        self.center = bool(center)
        self.below = bool(below)
        self.orientation = orientation
        self.offset = offset
        self.attributes = attributes

        self._template = Template(u"""
            {% macro script(this, kwargs) %}
                {{this.polyline.get_name()}}.setText("{{this.text}}", {
                    repeat: {{'true' if this.repeat else 'false'}},
                    center: {{'true' if this.center else 'false'}},
                    below: {{'true' if this.below else 'false'}},
                    offset: {{this.offset}},
                    orientation: {{this.orientation}},
                    attributes: {{this.attributes}}
                });
            {% endmacro %}
            """)  # noqa

    def render(self, **kwargs):
        super(PolyLineTextPath, self).render(**kwargs)

        figure = self.get_root()
        assert isinstance(figure, Figure), ('You cannot render this Element '
                                            'if it is not in a Figure.')

        figure.header.add_child(
            JavascriptLink("https://rawgit.com/makinacorpus/Leaflet.TextPath/leaflet0.8-dev/leaflet.textpath.js"),  # noqa
            name='polylinetextpath')
