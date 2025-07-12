import numpy as np
import plotly.graph_objects as go
from scipy.special import sph_harm
import plotly.io as pio
pio.renderers.default = 'browser' 



def Plot3DArmonicos(l,m,n=100, show=False, save_html=None):
    
    theta = np.linspace(0, np.pi, n)
    phi = np.linspace(0, 2*np.pi, n)
    theta_grid, phi_grid = np.meshgrid(theta, phi)
    x_grid = np.cos(theta_grid)
    
    ylm = sph_harm(m, l, phi_grid, theta_grid)
    

    if m == 0:
        A = np.real(ylm) 
        
    elif m > 0:
        A = np.real(ylm) 
    else:  
        A = np.imag(ylm) 
        
    r = np.abs(A)
    x = r * np.sin(theta_grid) * np.cos(phi_grid)
    y = r * np.sin(theta_grid) * np.sin(phi_grid)
    z = r * np.cos(theta_grid)

    max_r_val = np.max(r) if r.size > 0 and np.any(r) else 0

    plot_surfacecolor = np.real(A)
    plot_colorscale = 'Turbo' 
    plot_showscale = True
    abs_max_phase_val = np.max(np.abs(A)) if max_r_val > 0 else 1.0 
    plot_cmin = -abs_max_phase_val
    plot_cmax = abs_max_phase_val
    colorbar_title = "Amplitud"



    fig = go.Figure(data=[go.Surface(
        x=x, y=y, z=z,
        surfacecolor=plot_surfacecolor,
        colorscale=plot_colorscale,
        cmin=plot_cmin,
        cmax=plot_cmax,
        showscale=plot_showscale,
        colorbar=dict(title=colorbar_title, len=0.6, thickness=15, x=0.82, y=0.5) if plot_showscale else None,
        lighting=dict(ambient=0.3, diffuse=0.8, specular=0.3, roughness=0.4, fresnel=0.2),
        lightposition=dict(x=1000, y=1000, z=1000)
    )])

    title_str = f"Armónicos Esféricos: (l={l}, m={m})"

    fig.update_layout(
        title=dict(text=title_str, x=0.5, y=0.95, font_size=16),
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, zerolinewidth=1, zerolinecolor='black', showticklabels=False, title_text='', showbackground=False),
            yaxis=dict(showgrid=False, zeroline=False, zerolinewidth=1, zerolinecolor='black', showticklabels=False, title_text='', showbackground=False),
            zaxis=dict(showgrid=False, zeroline=False, zerolinewidth=1, zerolinecolor='black', showticklabels=False, title_text='', showbackground=False),
            bgcolor='white'
        ),
        scene_aspectmode='data', 
        scene_camera=dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0), eye=dict(x=1.5, y=1.5, z=1.0)),
        margin=dict(l=5, r=5, b=5, t=40)
    )

    if save_html:
        fig.write_html(save_html, auto_open=show)
    elif show:
        fig.show()
        
    return fig

Plot3DArmonicos(3,2,100,True)
