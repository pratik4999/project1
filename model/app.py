import json
import pandas as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

steel_model = pickle.load(open('steel_model.pkl', 'rb'))

plastics_model = pickle.load(open('plastics_model.pkl', 'rb'))

iron_model = pickle.load(open('iron_model.pkl', 'rb'))

aluminium_model = pickle.load(open('aluminium_model.pkl', 'rb'))

rubber_model = pickle.load(open('rubber_model.pkl', 'rb'))

glass_model = pickle.load(open('glass_model.pkl', 'rb'))

copper_model = pickle.load(open('copper_model.pkl', 'rb'))


@app.route('/')
def home():
       return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":
        startYear = request.form['startyear']
        endYear = request.form['endyear']
        # result3 = request.form['no_of_cars']
        difference = int(endYear) - int(startYear)
        
        result = []
        s = "value"
        for i in range(0,difference+1):
            res = (str(s)+str(i))
            result.append(request.form[res])
        
        # result_lenght = len(result)
        print(result)
        years_output = []
        years_output = result

        steel_output = []
        plastics_output = []
        iron_output = []
        rubber_output = []
        aluminium_output = []
        glass_output = []
        copper_output = []
        years_output = []
        
        years = []
        start = int(startYear)
        end = int(endYear)

        next = (start % 100) + 1
        snext = ''
        while start <= end:
            snext = str(start) +'-'+ str(format(next, '02d'))
            years.append(snext)
            start += 1
            next += 1


        for i in result:
            steel = steel_model.predict([[i]])
            steel_output.append(steel[0][0].round(2))
            
            plastics = plastics_model.predict([[i]])
            plastics_output.append(plastics[0][0].round(2))

            iron = iron_model.predict([[i]])
            iron_output.append(iron[0][0].round(2))
            
            rubber = rubber_model.predict([[i]])
            rubber_output.append(rubber[0][0].round(2))

            aluminium = aluminium_model.predict([[i]])
            aluminium_output.append(aluminium[0][0].round(2))

            glass =  glass_model.predict([[i]])
            glass_output.append(glass[0][0].round(2))

            copper = copper_model.predict([[i]])
            copper_output.append(copper[0][0].round(2))

            years_predict = []
            steel_predict = []
            plastic_predict = []
            iron_predict = []
            rubber_predict = []
            aluminium_predict = []
            glass_predict = []
            copper_predict = []


            years_predict =result 
            steel_predict = steel_output
            plastic_predict = plastics_output
            iron_predict = iron_output
            rubber_predict = rubber_output
            aluminium_predict = aluminium_output
            glass_predict = glass_output
            copper_predict = copper_output

           

            # print(years)
            print("All Output's")
            print(steel_predict)
            print(plastic_predict)
            print(iron_predict)
            print(rubber_predict)
            print(aluminium_predict)
            print(glass_predict)
            print(copper_predict)
            print(years_predict)

            # steel_list = list(itertools.product(steel_predict))
            # plastic_list = list(itertools.product(plastic_predict))
            # iron_list = list(itertools.product(iron_predict))
            # rubber_list = list(itertools.product(rubber_predict))
            # aluminium_list = list(itertools.product(aluminium_predict))
            # glass_list = list(itertools.product(glass_predict))
            # copper_list = list(itertools.product(copper_predict))
            # years_list = list(itertools.product(years_predict))
            # steel_table = ' '.join(steel_predict)
            # loop = 1

        return render_template("index.html", 
                                startYear=" Your Starting Year for Prediction is {} ".format(startYear),
                                endYear="Your Ending Year for Prediction is {} ".format(endYear),

                                steel_to_render = steel_predict ,
                                plastic_to_render = str(plastic_predict)[2:-3],
                                iron_to_render = str(iron_predict)[2:-3],
                           
                                rubber_to_render = str(rubber_predict)[1:-1],
                                aluminium_to_render = str(aluminium_predict)[1:-1],
                                glass_to_render = str(glass_predict)[1:-1],
                                copper_to_render = str(copper_predict)[1:-1],
                                years_to_render = str(years)[1:-1],
                                # years_to_render = years_list,
                                # loop = loop,
                                # year = '{} '.format(years),

                                # steel ='{}  '.format(steel_table),

                                # plastics=' {}  '.format(plastic_predict),

                                # iron=' {} '.format(iron_predict),

                                # rubber=' {} '.format(rubber_predict),
                            
                                # aluminium=' {} '.format(aluminium_predict),

                                # glass=' {} '.format(glass_predict),

                                # diff="Year Difference is {}".format(difference),

                                # copper=' {} tonnes'.format(copper_predict)
                                
                            )



if __name__ == '__main__':
   app.run(use_reloader = True,debug=True)
   