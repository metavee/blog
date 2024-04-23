"""Adapted from Set with Friends (https://setwithfriends.com) under the below license:

---

MIT License

Copyright (c) 2020 Eric Zhang, Cynthia Du

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

https://github.com/ekzhang/setwithfriends/blob/781e03116a309f155fa749b6272919d85a77605b/src/components/SetCard.js
https://github.com/ekzhang/setwithfriends/blob/781e03116a309f155fa749b6272919d85a77605b/public/index.html
"""

DEFINITIONS = """
      <defs>
        <path
          id="squiggle"
          d="m67.892902,12.746785c43.231313,-6.717223 107.352741,6.609823 121.028973,58.746408c13.676233,52.136585 -44.848649,161.467192 -45.07116,204.650732c4.566246,56.959708 83.805481,87.929227 22.329944,105.806022c-61.475536,17.876795 -126.122496,-1.855045 -143.73294,-41.933823c-17.610444,-40.07878 49.274638,-120.109409 46.14822,-188.091997c-3.126418,-67.982588 -21.873669,-70.257464 -49.613153,-80.177084c-27.739485,-9.919618 5.678801,-52.283035 48.910115,-59.000258z"
        />
        <path
          id="oval"
          d="m11.49999,95.866646c0,-44.557076 37.442923,-81.999998 82.000002,-81.999998l12.000015,0c44.557076,0 81.999992,37.442923 81.999992,81.999998l0,206.133354c0,44.557098 -37.442917,82 -81.999992,82l-12.000015,0c-44.557079,0 -82.000002,-37.442902 -82.000002,-82l0,-206.133354z"
        />
        <path
          id="diamond"
          d="m98.544521,10.311863l-87.830189,189.330815l88.201143,189.644391l88.942329,-190.362741l-89.313283,-188.612465z"
        />
        <pattern
          id="pattern-stripe"
          width="2"
          height="20"
          patternUnits="userSpaceOnUse"
        >
          <rect width="2" height="8" fill="#fff" />
        </pattern>
        <mask id="mask-stripe">
          <rect
            x="0"
            y="0"
            width="200"
            height="400"
            fill="url(#pattern-stripe)"
          />
        </mask>
      </defs>
"""

COLORS = {"purple": '#800080', "green": '#008000', "red": '#FF0000'}
SHAPES = ['squiggle', 'oval', 'diamond']
SHADES = ['filled', 'outlined', 'striped']

def generate_svg(color_val, shape_id, shade_id, number, scale=1.0, margin=30.0):
    assert shade_id in SHADES
    assert number in [0, 1, 2, 3]
    assert shape_id in SHAPES

    # Adjust the scale based
    scaled_width = 100 * scale
    scaled_height = 200 * scale
    spacing = 10 * scale  # Space between shapes

    total_width = (scaled_width + spacing) * 3 - spacing  # Total width calculations
    viewBox_width = total_width / scale
    viewBox_height = scaled_height / scale

    svg_str = f'<svg width="{total_width}" height="{scaled_height}" viewBox="{-margin} {-margin} {viewBox_width + 2*margin} {viewBox_height + 2*margin}" xmlns="http://www.w3.org/2000/svg">'
    svg_str += DEFINITIONS

    def svg_helper(shape_id, transform, fill, stroke="none", mask=None):
        stroke_width = "20" if stroke != "none" else "0"  # Adjust strokeWidth to account for scale

        if mask:
            mask_str = f'mask="{mask}"'
        else:
            mask_str = ""
        
        return f'<use href="#{shape_id}" transform="{transform}" fill="{fill}" {mask_str} stroke="{stroke}" stroke-width="{stroke_width}"/>'

    for i in range(number):
        x_offset = i * (viewBox_width / (number))  # Distribute shapes evenly across the viewBox
        transform = f"translate({x_offset}, 0) scale({scale})"  # Adjust transform for position and scale

        if shade_id == 'filled':
            svg_str += svg_helper(shape_id, transform, fill=color_val)

        if shade_id in ['outlined', 'striped']:  # draw outline
            svg_str += svg_helper(shape_id, transform, stroke=color_val, fill="none")

        if shade_id == 'striped':
            svg_str += svg_helper(shape_id, transform, fill=color_val, mask='url(#mask-stripe)')

    # Append a rounded rectangle with a thin black stroke around the canvas
    border_stroke_width = 2  # Adjust the stroke width as needed
    # Assuming a 10% radius for rounded corners relatively to the height, adjust as needed
    radius = viewBox_height * 0.1
    # Subtract half stroke width from dimensions to ensure the stroke fits within the viewbox
    rect_width = viewBox_width - border_stroke_width
    rect_height = viewBox_height - border_stroke_width
    # svg_str += f'<rect x="{border_stroke_width/2}" y="{border_stroke_width/2}" width="{rect_width}" height="{rect_height}" rx="{radius}" ry="{radius}" fill="none" stroke="black" stroke-width="{border_stroke_width}"/>'

    svg_str += '</svg>'
    return svg_str

# Render all cards
for number in [1, 2, 3]:
    for color_name, color_val in COLORS.items():
        for shape in SHAPES:
            for shade in SHADES:
                with open(f"{number}_{color_name}_{shade}_{shape}.svg", "w") as ofile:
                    ofile.write(generate_svg(color_val, shape, shade, number, scale=0.5))

# Also render a blank
with open("blank.svg", "w") as ofile:
    ofile.write(generate_svg(color_val, shape, shade, 0, scale=0.5))
