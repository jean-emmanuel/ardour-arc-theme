import re

colors = {
    'arc-background-dark': '#171a1d',
    'arc-background': '#2E3440',
    'arc-background-alt': '#2E3440',
    'arc-foreground': '#3B4252',
    'arc-text': '#D8DEE9',
    'arc-text-dark': '#9ea2ab',
    'arc-text-darker': '#707379',
    'arc-red': '#BF616A',
    'arc-red-dark': '#944d54',
    'arc-orange': '#D08770',
    'arc-yellow': '#EBCB8B',
    'arc-green': '#8cbe8c',
    'arc-green-dark': '#608260',
    'arc-green-ish': '#364036',
    'arc-blue': '#5E81AC',
    'arc-blue-dark': '#445d7b',
    'arc-blue-ish': '#263242',
    'arc-cyan': '#88C0D0',
    'arc-gray': '#f57980',
    'arc-undef': '#ff00ff',
    'arc-grid-major': '#9ea2ab',
    'arc-grid-minor': '#707379',
    'arc-grid-micro': '#4d4e52',
}

def repl(m):
    color = m.group(1)
    if color in colors:
        return 'value="%s"' % (colors[color].replace('#', '') + 'ff')
    else:
        return 'value="%s"' % color

with open('arc-ardour.colors.in', 'r') as source_file:
    with open('arc-ardour.colors', 'w') as dest_file:
        dest = ''
        for line in source_file:
            dest += re.sub('value="([^\"]*)"', repl, line)
        dest_file.write(dest)
