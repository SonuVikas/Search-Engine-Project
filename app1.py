import pandas as pd
from flask import Flask, render_template, request


df = pd.read_csv(r"C:\Users\dell\Desktop\Internship 2024\Search Engine project internship\final_data_searchengine.csv")

# Fill NaN values in 'Movies&WebSeries' column with an empty string
df['title'].fillna('', inplace=True)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_text = request.form.get("search_text")
        if search_text:
            # Filter the DataFrame and handle NaN values in 'title' column
            results = df[df['clean_content'].str.contains(search_text, case=False)]['title'].tolist()
            return render_template("results.html", search_text=search_text, results=results)
        else:
            return render_template("results.html", search_text="Nothing", results=None)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)