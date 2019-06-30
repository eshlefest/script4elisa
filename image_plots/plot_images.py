import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
from scipy.signal import savgol_filter

import plotly
plotly.tools.set_credentials_file(username='your-username', api_key='your-api-key')

# simulate spectroscopy data
def simulated_absorption(mu, sigma, intensity):
    data = [np.random.normal(mu[i], sigma[i], intensity[i]) for i in range(len(mu))]
    hists = [np.histogram(d, 1000, range=(200, 500), normed=True) for d in data]
    ys = [y for y, x in hists]
    s = savgol_filter(np.max(ys, axis=0), 41, 3)
    return hists[0][1], s


mus = [[1, 1, 1], [1, 1]]
sigmas = [[4, 6, 10], [5, 4]]
intensities = [[100000, 300000, 700000], [40000, 20000]]

simulated_absorptions = [simulated_absorption(m, s, i) for m, s, i in zip(mus, sigmas, intensities)]
print simulated_absorptions

# create traces from data
names = ['Benzene', 'Naphthalene']
colors = ['red', 'maroon']
traces = [go.Scatter(x=x, y=y, name=n, line=dict(color=c)) for (x, y), n, c in
          zip(simulated_absorptions, names, colors)]

# add pictures using layout-images and then connect the image to its trace using annotations
layout = go.Layout(
    images=[dict(
        source="https://raw.githubusercontent.com/eshlefest/script4elisa/master/image_plots/images/elisa.jpeg",
        xref="paper",
        yref="paper",
        x=0.1,
        y=0.1,
        sizex=0.3,
        sizey=0.3,
        xanchor="right",
        yanchor="bottom"
    ), dict(
        source="https://raw.githubusercontent.com/eshlefest/script4elisa/master/image_plots/images/ryan-photo.jpg",
        xref="paper",
        yref="paper",
        x=0.9,
        y=0.9,
        sizex=0.3,
        sizey=0.3,

        xanchor="right",
        yanchor="bottom"
    )
    ],
    title='Cool Factor',
    yaxis=dict(hoverformat='.3f', title='Coolness'),
    xaxis=dict(title='Radness'),
    showlegend=False,
    height=500,
    width=900

)

fig = go.Figure(data=traces, layout=layout)
py.iplot(fig, filename='ryan-1')