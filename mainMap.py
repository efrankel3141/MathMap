from pyvis.network import Network

net = Network(height="100vh", width="100%",  bgcolor="#121212f0f0f0", font_color="ffffff")

# Create a network
net = Network(directed=False)

default_properties = {
        "shape": "square",
        "color": "#115178",
        "size": 30,
        "font": {"color": "black", "size": 20, "face": "arial"},
        "borderWidth": 2,
    }
# Merge default properties with any custom properties
node_properties = {**default_properties, **custom_properties}

def add_field(net, net.len(nodes), label, **custom_properties):
    """
    Add a node with consistent styling, allowing optional overrides.
    
    Args:
        network (Network): Pyvis network object.
        node_id (int or str): Unique identifier for the node.
        label (str): Label text for the node.
        custom_properties (dict): Optional overrides for node styling.
    """


# Save the HTML file only
html_file = "mindmap.html"
try:
    net.write_html(html_file)  # Write directly to HTML without rendering
    print(f"Mindmap created successfully: {html_file}")
except Exception as e:
    print(f"Failed to create the mindmap: {e}")