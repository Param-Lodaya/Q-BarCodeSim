import plotly.graph_objects as go
from plotly.offline import plot
import plotly.io as pio

def create_cuboid(x, y, z, dx, dy, dz, color, opacity):
    vertices = [
        [x, y, z], [x+dx, y, z], [x+dx, y+dy, z], [x, y+dy, z],
        [x, y, z+dz], [x+dx, y, z+dz], [x+dx, y+dy, z+dz], [x, y+dy, z+dz]
    ]
    faces = [
        [0, 1, 2], [0, 2, 3],
        [4, 5, 6], [4, 6, 7],
        [0, 1, 5], [0, 5, 4],
        [2, 3, 7], [2, 7, 6],
        [1, 2, 6], [1, 6, 5],
        [3, 0, 4], [3, 4, 7]
    ]
    x_vals, y_vals, z_vals = zip(*vertices)
    i, j, k = zip(*faces)

    return go.Mesh3d(
        x=x_vals, y=y_vals, z=z_vals,
        i=i, j=j, k=k,
        color=color,
        opacity=opacity,
        flatshading=True,
        showscale=False
    )

def visualize_barcode(visual_data, filename="quantum_barcode_3d.html"):
    fig = go.Figure()
    spacing = 3
    default_opacity = 0.95

    for i, entry in enumerate(visual_data):
        x = i * spacing
        y = 0
        z = 0
        dx = entry['width']
        dy = 0.8
        dz = entry['height']
        color = entry['colour']
        opacity = max(entry['brightness'], default_opacity)
        bitstring = entry['bitsize']

        fig.add_trace(create_cuboid(x, y, z, dx, dy, dz, color, opacity))

        fig.add_trace(go.Scatter3d(
            x=[x + dx / 2],
            y=[y + dy / 2],
            z=[z + dz + 10],
            mode='text',
            text=[f"|{bitstring}⟩"],
            textposition='top center',
            showlegend=False
        ))

    fig.update_layout(
        title="Quantum Barcode Visualization (3D Cuboids + Floating State Labels)",
        scene=dict(
            xaxis_title="Qubit State Index",
            yaxis_title="Depth",
            zaxis_title="Measurement Frequency",
            camera=dict(eye=dict(x=1.6, y=1.2, z=1.2))
        ),
        margin=dict(l=10, r=10, t=40, b=10)
    )

    # Show the interactive plot
    fig.show()

    # Save as HTML
    fig.write_html(filename)
    print(f" HTML file saved to: {filename}")

    # Save as PNG using Kaleido
    try:
        fig.write_image("QBarCode_Seal.png")
        print(" PNG image saved: QBarCode_Seal.png")
    except Exception as e:
        print(" PNG export failed. Is 'kaleido' installed?")
        print("Error:", e)