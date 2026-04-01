# ---------- IMPORTS ----------
from mean_var_std import calculate
from demographic_data_analyzer import calculate_demographic_data
from medical_data_visualizer import draw_cat_plot, draw_heat_map
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
from sea_level_predictor import draw_plot


# ---------- MAIN EXECUTION ----------
def run_all_projects():

    print("\n🔢 Running Matrix Statistics Engine...")
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    result = calculate(numbers)
    print(result)

    print("\n👥 Running Demographic Data Analyzer...")
    calculate_demographic_data()

    print("\n❤️ Running Medical Data Visualizer...")
    cat_fig = draw_cat_plot()
    heat_fig = draw_heat_map()
    cat_fig.savefig("catplot.png")
    heat_fig.savefig("heatmap.png")
    print("Medical plots saved!")

    print("\n📈 Running Time Series Visualizer...")
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    print("Time series plots saved!")

    print("\n🌊 Running Sea Level Predictor...")
    draw_plot()
    print("Sea level plot saved!")

    print("\n✅ All projects executed successfully!")


# ---------- RUN ----------
if __name__ == "__main__":
    run_all_projects()
