from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            total_rent = float(request.form["total_rent"])
            society_maintenance = float(request.form["society_maintenance"])
            water_bill = float(request.form["water_bill"])
            electricity_bill = float(request.form["electricity_bill"])
            total_food = float(request.form["total_food"])
            people = int(request.form["people"])

            if people == 0:
                error = "Number of people cannot be zero!"
            else:
                total_amount = total_rent + society_maintenance + water_bill + electricity_bill + total_food
                result = total_amount / people

        except ValueError:
            error = "Invalid input! Please enter valid numbers."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
