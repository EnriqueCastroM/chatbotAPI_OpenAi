from flask import Flask, redirect, render_template, request, url_for
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":

        prompt_form = request.form["prompt"]
        engine_model_gpt3 = "text-davinci-003" 
        completion = openai.Completion.create(
        engine = engine_model_gpt3,
        prompt = prompt_form,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.5
        )
        return redirect(url_for("index", result=completion.choices[0].text))

    result = request.args.get("result")
    historial= []
    historial.append(result)
    print(historial)
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
