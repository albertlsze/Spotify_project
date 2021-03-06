import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.io import output_notebook, show, output_file
from bokeh.models import ColumnDataSource, HoverTool, Panel
from bokeh.models.widgets import Tabs
from pprint import pprint

class bokeh_hist():
    def __init__(self,title):
        self.hists = []
        output_file(f"{title}.html")

    def add_tabs(self,data:pd,features:list,show_plot=False)->None:
        '''
        This function create a histogram with multiple tabs

        :param data: pandas data frame of data
        :param features: items in data to create histogram
        :param show_plot: boolean to show plot or not
        :return: None
        '''
        for column in features:
            plot = self.hist_hover(data,column,show_plot=show_plot)
            panel = Panel(child=plot,title=column.capitalize())
            self.hists.append(panel)
        t= Tabs(tabs=self.hists)
        show(t)

    def hist_hover(self,data:pd, column:str, bins=30, show_plot=True):
        '''
        This function creates a bokeh histogram plot

        :param data: pandas data frame of data
        :param column: data to be plotted
        :param bins: number of bins for the histogram
        :param show_plot: boolean to show histogram plot
        :return: plot
        '''
        curdoc().theme = 'dark_minimal'
        hist, edges = np.histogram(data[column], bins = bins)

        hist_df = pd.DataFrame({column: hist,
                                "left": edges[:-1],
                                "right": edges[1:]})
        hist_df["interval"] = [f"{round(left,3)} to {round(right,3)}" for left,right in zip(hist_df["left"], hist_df["right"])]

        src = ColumnDataSource(hist_df)

        plot = figure(plot_height = 600, plot_width = 1000,
              title = f"Histogram of {column}",
              x_axis_label = column.capitalize(),
              y_axis_label = "Count")
        plot.quad(bottom = 0, top = column,left = "left",
            right = "right", source = src, fill_color = 'forestgreen',
            line_color = "black", fill_alpha = 0.7,
            hover_fill_alpha = 1.0, hover_fill_color = 'Tan')

        hover = HoverTool(tooltips = [('Interval', '@interval'),
                                  ('Count', f"@{column}")])
        plot.add_tools(hover)

        if show_plot == True:
            show(plot)
        else:
            return plot

if __name__ == "__main__":
    song_data = 'D:\\Documents\\Github\\albertlsze\\Spotify_project\\scripts\\Prepopulated_data\\song_data.csv'
    song_data = pd.read_csv(song_data)
    column = ["acousticness","danceability","duration_ms","energy","instrumentalness","key","liveness","loudness","popularity","speechiness","tempo","valence"]

    graph = bokeh_hist("Song Features")
    graph.add_tabs(song_data,column)