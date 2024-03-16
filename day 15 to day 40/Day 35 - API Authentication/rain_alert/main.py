import requests
import datetime as dt
from info import OWM_Endpoint, api_key
from twilio_api import send_sms

parameters = {
    "lat": -14.235004,
    "lon": -51.925282,
    "cnt": 1,
    "appid": api_key
}

# response = requests.get(url=OWM_Endpoint, params=parameters)
# response.raise_for_status()
#
# response = response.json()
# as I had only one request to do by day, I will continue my code with the result in the variable
response = {"lat":-14.235,"lon":-51.9253,"timezone":"America/Cuiaba","timezone_offset":-14400,"current":{"dt":1710600870,"sunrise":1710581477,"sunset":1710625272,"temp":306.89,"feels_like":311.64,"pressure":1010,"humidity":52,"dew_point":295.66,"uvi":14.24,"clouds":31,"visibility":10000,"wind_speed":1.99,"wind_deg":37,"wind_gust":2.52,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}]},"minutely":[{"dt":1710600900,"precipitation":0},{"dt":1710600960,"precipitation":0},{"dt":1710601020,"precipitation":0},{"dt":1710601080,"precipitation":0},{"dt":1710601140,"precipitation":0},{"dt":1710601200,"precipitation":0},{"dt":1710601260,"precipitation":0},{"dt":1710601320,"precipitation":0},{"dt":1710601380,"precipitation":0},{"dt":1710601440,"precipitation":0},{"dt":1710601500,"precipitation":0},{"dt":1710601560,"precipitation":0},{"dt":1710601620,"precipitation":0},{"dt":1710601680,"precipitation":0},{"dt":1710601740,"precipitation":0},{"dt":1710601800,"precipitation":0},{"dt":1710601860,"precipitation":0},{"dt":1710601920,"precipitation":0},{"dt":1710601980,"precipitation":0},{"dt":1710602040,"precipitation":0},{"dt":1710602100,"precipitation":0},{"dt":1710602160,"precipitation":0},{"dt":1710602220,"precipitation":0},{"dt":1710602280,"precipitation":0},{"dt":1710602340,"precipitation":0},{"dt":1710602400,"precipitation":0},{"dt":1710602460,"precipitation":0},{"dt":1710602520,"precipitation":0},{"dt":1710602580,"precipitation":0},{"dt":1710602640,"precipitation":0},{"dt":1710602700,"precipitation":0},{"dt":1710602760,"precipitation":0},{"dt":1710602820,"precipitation":0},{"dt":1710602880,"precipitation":0},{"dt":1710602940,"precipitation":0},{"dt":1710603000,"precipitation":0},{"dt":1710603060,"precipitation":0},{"dt":1710603120,"precipitation":0},{"dt":1710603180,"precipitation":0},{"dt":1710603240,"precipitation":0},{"dt":1710603300,"precipitation":0},{"dt":1710603360,"precipitation":0},{"dt":1710603420,"precipitation":0},{"dt":1710603480,"precipitation":0},{"dt":1710603540,"precipitation":0},{"dt":1710603600,"precipitation":0},{"dt":1710603660,"precipitation":0},{"dt":1710603720,"precipitation":0},{"dt":1710603780,"precipitation":0},{"dt":1710603840,"precipitation":0},{"dt":1710603900,"precipitation":0},{"dt":1710603960,"precipitation":0},{"dt":1710604020,"precipitation":0},{"dt":1710604080,"precipitation":0},{"dt":1710604140,"precipitation":0},{"dt":1710604200,"precipitation":0},{"dt":1710604260,"precipitation":0},{"dt":1710604320,"precipitation":0},{"dt":1710604380,"precipitation":0},{"dt":1710604440,"precipitation":0}],"hourly":[{"dt":1710597600,"temp":306.73,"feels_like":311.62,"pressure":1010,"humidity":53,"dew_point":295.83,"uvi":12.05,"clouds":32,"visibility":10000,"wind_speed":1.13,"wind_deg":68,"wind_gust":1.91,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.45,"rain":{"1h":0.25}},{"dt":1710601200,"temp":306.89,"feels_like":311.64,"pressure":1010,"humidity":52,"dew_point":295.66,"uvi":14.24,"clouds":31,"visibility":10000,"wind_speed":1.99,"wind_deg":37,"wind_gust":2.52,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.54},{"dt":1710604800,"temp":306.97,"feels_like":311.48,"pressure":1010,"humidity":51,"dew_point":295.42,"uvi":14.13,"clouds":30,"visibility":10000,"wind_speed":2.3,"wind_deg":26,"wind_gust":2.93,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.5},{"dt":1710608400,"temp":307.3,"feels_like":311.87,"pressure":1009,"humidity":50,"dew_point":295.39,"uvi":11.68,"clouds":27,"visibility":10000,"wind_speed":2.01,"wind_deg":13,"wind_gust":2.94,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.46,"rain":{"1h":0.42}},{"dt":1710612000,"temp":307.56,"feels_like":311.42,"pressure":1008,"humidity":47,"dew_point":294.62,"uvi":7.88,"clouds":26,"visibility":10000,"wind_speed":1.96,"wind_deg":357,"wind_gust":2.95,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.46},{"dt":1710615600,"temp":306.23,"feels_like":310.51,"pressure":1007,"humidity":53,"dew_point":295.37,"uvi":4,"clouds":57,"visibility":10000,"wind_speed":2.29,"wind_deg":353,"wind_gust":3.62,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0.17},{"dt":1710619200,"temp":303.81,"feels_like":308.51,"pressure":1006,"humidity":65,"dew_point":296.62,"uvi":1.34,"clouds":66,"visibility":10000,"wind_speed":2.09,"wind_deg":4,"wind_gust":5.46,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"pop":0.2},{"dt":1710622800,"temp":302.88,"feels_like":308.48,"pressure":1007,"humidity":74,"dew_point":297.6,"uvi":0.2,"clouds":49,"visibility":10000,"wind_speed":0.75,"wind_deg":304,"wind_gust":1.21,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.18},{"dt":1710626400,"temp":300.47,"feels_like":303.5,"pressure":1008,"humidity":79,"dew_point":296.52,"uvi":0,"clouds":61,"visibility":10000,"wind_speed":1.19,"wind_deg":25,"wind_gust":1.84,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.18},{"dt":1710630000,"temp":299.56,"feels_like":299.56,"pressure":1009,"humidity":81,"dew_point":296.1,"uvi":0,"clouds":69,"visibility":10000,"wind_speed":0.19,"wind_deg":329,"wind_gust":0.66,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.18},{"dt":1710633600,"temp":299.22,"feels_like":299.22,"pressure":1009,"humidity":82,"dew_point":295.86,"uvi":0,"clouds":65,"visibility":10000,"wind_speed":0.65,"wind_deg":320,"wind_gust":0.73,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.16},{"dt":1710637200,"temp":299.69,"feels_like":299.69,"pressure":1010,"humidity":78,"dew_point":295.56,"uvi":0,"clouds":92,"visibility":10000,"wind_speed":1.2,"wind_deg":30,"wind_gust":1.59,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0.16},{"dt":1710640800,"temp":299.53,"feels_like":299.53,"pressure":1010,"humidity":79,"dew_point":295.55,"uvi":0,"clouds":89,"visibility":10000,"wind_speed":0.99,"wind_deg":81,"wind_gust":1.24,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0.04},{"dt":1710644400,"temp":298.27,"feels_like":299.06,"pressure":1010,"humidity":85,"dew_point":295.57,"uvi":0,"clouds":65,"visibility":10000,"wind_speed":0.95,"wind_deg":67,"wind_gust":1.12,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.04},{"dt":1710648000,"temp":297.78,"feels_like":298.6,"pressure":1010,"humidity":88,"dew_point":295.66,"uvi":0,"clouds":71,"visibility":10000,"wind_speed":1.06,"wind_deg":43,"wind_gust":1.22,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.06},{"dt":1710651600,"temp":297.47,"feels_like":298.28,"pressure":1010,"humidity":89,"dew_point":295.61,"uvi":0,"clouds":77,"visibility":10000,"wind_speed":1.23,"wind_deg":29,"wind_gust":1.56,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.14},{"dt":1710655200,"temp":297.3,"feels_like":298.12,"pressure":1010,"humidity":90,"dew_point":295.55,"uvi":0,"clouds":80,"visibility":10000,"wind_speed":1.29,"wind_deg":12,"wind_gust":2.28,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.25},{"dt":1710658800,"temp":296.93,"feels_like":297.77,"pressure":1010,"humidity":92,"dew_point":295.47,"uvi":0,"clouds":81,"visibility":10000,"wind_speed":1.33,"wind_deg":13,"wind_gust":2.62,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"pop":0.58,"rain":{"1h":0.14}},{"dt":1710662400,"temp":296.59,"feels_like":297.44,"pressure":1011,"humidity":94,"dew_point":295.48,"uvi":0,"clouds":52,"visibility":10000,"wind_speed":1.18,"wind_deg":12,"wind_gust":2.1,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.75},{"dt":1710666000,"temp":296.38,"feels_like":297.24,"pressure":1011,"humidity":95,"dew_point":295.4,"uvi":0,"clouds":41,"visibility":10000,"wind_speed":0.99,"wind_deg":357,"wind_gust":1.21,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0.7},{"dt":1710669600,"temp":296.84,"feels_like":297.69,"pressure":1012,"humidity":93,"dew_point":295.49,"uvi":0.24,"clouds":36,"visibility":10000,"wind_speed":0.89,"wind_deg":336,"wind_gust":1.49,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.67},{"dt":1710673200,"temp":298.95,"feels_like":299.75,"pressure":1013,"humidity":83,"dew_point":295.81,"uvi":1.5,"clouds":35,"visibility":10000,"wind_speed":1.42,"wind_deg":340,"wind_gust":2.9,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.63},{"dt":1710676800,"temp":301.21,"feels_like":304.49,"pressure":1013,"humidity":74,"dew_point":296.01,"uvi":4.29,"clouds":35,"visibility":10000,"wind_speed":1.26,"wind_deg":340,"wind_gust":2.18,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.59},{"dt":1710680400,"temp":303.18,"feels_like":307.32,"pressure":1013,"humidity":66,"dew_point":296.22,"uvi":8.14,"clouds":80,"visibility":10000,"wind_speed":1.39,"wind_deg":354,"wind_gust":2.29,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.24,"rain":{"1h":0.27}},{"dt":1710684000,"temp":304.97,"feels_like":309.52,"pressure":1013,"humidity":59,"dew_point":295.99,"uvi":12.04,"clouds":83,"visibility":10000,"wind_speed":1.52,"wind_deg":351,"wind_gust":2.28,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.38,"rain":{"1h":0.37}},{"dt":1710687600,"temp":305.98,"feels_like":310.58,"pressure":1012,"humidity":55,"dew_point":295.74,"uvi":14.19,"clouds":61,"visibility":10000,"wind_speed":1.97,"wind_deg":355,"wind_gust":2.34,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"pop":0.42,"rain":{"1h":0.43}},{"dt":1710691200,"temp":306.51,"feels_like":310.48,"pressure":1011,"humidity":51,"dew_point":295.04,"uvi":14.04,"clouds":50,"visibility":10000,"wind_speed":2.37,"wind_deg":357,"wind_gust":2.31,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.49},{"dt":1710694800,"temp":306.72,"feels_like":310.62,"pressure":1010,"humidity":50,"dew_point":294.82,"uvi":10.85,"clouds":44,"visibility":10000,"wind_speed":2.53,"wind_deg":359,"wind_gust":2.31,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.49},{"dt":1710698400,"temp":306.56,"feels_like":310.28,"pressure":1009,"humidity":50,"dew_point":294.89,"uvi":5.45,"clouds":39,"visibility":10000,"wind_speed":2.42,"wind_deg":0,"wind_gust":2.04,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],"pop":0.49},{"dt":1710702000,"temp":306.05,"feels_like":309.82,"pressure":1008,"humidity":52,"dew_point":295.12,"uvi":1.83,"clouds":19,"visibility":10000,"wind_speed":2.24,"wind_deg":357,"wind_gust":1.8,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"pop":0.07},{"dt":1710705600,"temp":305.11,"feels_like":309.54,"pressure":1008,"humidity":58,"dew_point":296.02,"uvi":0.58,"clouds":19,"visibility":10000,"wind_speed":1.96,"wind_deg":357,"wind_gust":1.68,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"pop":0.02},{"dt":1710709200,"temp":302.74,"feels_like":307.88,"pressure":1009,"humidity":73,"dew_point":297.43,"uvi":0.13,"clouds":17,"visibility":10000,"wind_speed":1.55,"wind_deg":358,"wind_gust":3.47,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02d"}],"pop":0.15},{"dt":1710712800,"temp":300.47,"feels_like":303.5,"pressure":1009,"humidity":79,"dew_point":296.45,"uvi":0,"clouds":15,"visibility":10000,"wind_speed":1.21,"wind_deg":343,"wind_gust":1.33,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"pop":0.19},{"dt":1710716400,"temp":299.87,"feels_like":302.28,"pressure":1010,"humidity":80,"dew_point":296.03,"uvi":0,"clouds":12,"visibility":10000,"wind_speed":1.49,"wind_deg":15,"wind_gust":2.1,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"pop":0.26},{"dt":1710720000,"temp":299.45,"feels_like":299.45,"pressure":1010,"humidity":81,"dew_point":295.8,"uvi":0,"clouds":11,"visibility":10000,"wind_speed":1.37,"wind_deg":16,"wind_gust":1.37,"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"pop":0.31},{"dt":1710723600,"temp":299.08,"feels_like":299.87,"pressure":1010,"humidity":82,"dew_point":295.69,"uvi":0,"clouds":37,"visibility":10000,"wind_speed":1.19,"wind_deg":20,"wind_gust":1.43,"weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03n"}],"pop":0.25},{"dt":1710727200,"temp":298.65,"feels_like":299.45,"pressure":1011,"humidity":84,"dew_point":295.71,"uvi":0,"clouds":66,"visibility":10000,"wind_speed":1.37,"wind_deg":21,"wind_gust":1.44,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.45},{"dt":1710730800,"temp":298.34,"feels_like":299.16,"pressure":1011,"humidity":86,"dew_point":295.78,"uvi":0,"clouds":77,"visibility":10000,"wind_speed":1.35,"wind_deg":13,"wind_gust":1.72,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.45},{"dt":1710734400,"temp":298.16,"feels_like":298.99,"pressure":1010,"humidity":87,"dew_point":295.85,"uvi":0,"clouds":83,"visibility":10000,"wind_speed":1.24,"wind_deg":11,"wind_gust":1.4,"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"pop":0.45},{"dt":1710738000,"temp":298.18,"feels_like":299.01,"pressure":1010,"humidity":87,"dew_point":295.84,"uvi":0,"clouds":86,"visibility":10000,"wind_speed":0.82,"wind_deg":12,"wind_gust":0.89,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0.29},{"dt":1710741600,"temp":297.93,"feels_like":298.76,"pressure":1010,"humidity":88,"dew_point":295.76,"uvi":0,"clouds":89,"visibility":10000,"wind_speed":0.85,"wind_deg":17,"wind_gust":0.86,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0.31},{"dt":1710745200,"temp":297.64,"feels_like":298.44,"pressure":1010,"humidity":88,"dew_point":295.53,"uvi":0,"clouds":95,"visibility":10000,"wind_speed":0.81,"wind_deg":343,"wind_gust":0.86,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1710748800,"temp":297.36,"feels_like":298.16,"pressure":1010,"humidity":89,"dew_point":295.35,"uvi":0,"clouds":87,"visibility":10000,"wind_speed":0.9,"wind_deg":330,"wind_gust":0.94,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0},{"dt":1710752400,"temp":297.57,"feels_like":298.34,"pressure":1010,"humidity":87,"dew_point":295.25,"uvi":0,"clouds":87,"visibility":10000,"wind_speed":0.67,"wind_deg":337,"wind_gust":0.71,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"pop":0.06},{"dt":1710756000,"temp":297.92,"feels_like":298.7,"pressure":1011,"humidity":86,"dew_point":295.31,"uvi":0.14,"clouds":90,"visibility":10000,"wind_speed":0.63,"wind_deg":48,"wind_gust":0.62,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.15},{"dt":1710759600,"temp":299.31,"feels_like":299.31,"pressure":1012,"humidity":81,"dew_point":295.74,"uvi":1.35,"clouds":86,"visibility":10000,"wind_speed":0.82,"wind_deg":67,"wind_gust":1.52,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.21},{"dt":1710763200,"temp":301.27,"feels_like":304.33,"pressure":1013,"humidity":72,"dew_point":295.63,"uvi":3.97,"clouds":85,"visibility":10000,"wind_speed":1.46,"wind_deg":56,"wind_gust":2.53,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.21},{"dt":1710766800,"temp":300.63,"feels_like":303.28,"pressure":1013,"humidity":74,"dew_point":295.68,"uvi":7.84,"clouds":97,"visibility":10000,"wind_speed":1.12,"wind_deg":15,"wind_gust":2.24,"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"pop":0.18}],"daily":[{"dt":1710601200,"sunrise":1710581477,"sunset":1710625272,"moonrise":1710603420,"moonset":1710644340,"moon_phase":0.23,"summary":"Expect a day of partly cloudy with rain","temp":{"day":306.89,"min":296.18,"max":307.56,"night":298.27,"eve":302.88,"morn":296.47},"feels_like":{"day":311.64,"night":299.06,"eve":308.48,"morn":297.29},"pressure":1010,"humidity":52,"dew_point":295.66,"wind_speed":2.3,"wind_deg":26,"wind_gust":5.46,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":31,"pop":0.78,"rain":3.64,"uvi":14.24},{"dt":1710687600,"sunrise":1710667883,"sunset":1710711630,"moonrise":1710693180,"moonset":1710734040,"moon_phase":0.25,"summary":"Expect a day of partly cloudy with rain","temp":{"day":305.98,"min":296.38,"max":306.72,"night":298.34,"eve":302.74,"morn":296.38},"feels_like":{"day":310.58,"night":299.16,"eve":307.88,"morn":297.24},"pressure":1012,"humidity":55,"dew_point":295.74,"wind_speed":2.53,"wind_deg":359,"wind_gust":3.47,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":61,"pop":0.75,"rain":1.21,"uvi":14.19},{"dt":1710774000,"sunrise":1710754288,"sunset":1710797987,"moonrise":1710782820,"moonset":0,"moon_phase":0.3,"summary":"Expect a day of partly cloudy with rain","temp":{"day":306.14,"min":297.36,"max":307.67,"night":297.71,"eve":303.06,"morn":297.57},"feels_like":{"day":310.31,"night":298.49,"eve":308.21,"morn":298.34},"pressure":1011,"humidity":53,"dew_point":295.3,"wind_speed":1.84,"wind_deg":7,"wind_gust":2.62,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":71,"pop":0.62,"rain":0.93,"uvi":14.09},{"dt":1710860400,"sunrise":1710840694,"sunset":1710884345,"moonrise":1710872100,"moonset":1710823800,"moon_phase":0.33,"summary":"Expect a day of partly cloudy with rain","temp":{"day":306.48,"min":295.97,"max":306.48,"night":298.34,"eve":303.05,"morn":295.97},"feels_like":{"day":310.73,"night":299.13,"eve":308.43,"morn":296.76},"pressure":1011,"humidity":52,"dew_point":295.3,"wind_speed":1.91,"wind_deg":338,"wind_gust":5.43,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":60,"pop":0.6,"rain":0.92,"uvi":13.92},{"dt":1710946800,"sunrise":1710927100,"sunset":1710970702,"moonrise":1710961140,"moonset":1710913440,"moon_phase":0.36,"summary":"Expect a day of partly cloudy with rain","temp":{"day":306.36,"min":296.67,"max":306.62,"night":298.65,"eve":302.78,"morn":296.67},"feels_like":{"day":310.47,"night":299.34,"eve":307.75,"morn":297.45},"pressure":1009,"humidity":52,"dew_point":295.26,"wind_speed":2.25,"wind_deg":328,"wind_gust":4.13,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":95,"pop":0.4,"rain":0.42,"uvi":4.22},{"dt":1711033200,"sunrise":1711013505,"sunset":1711057059,"moonrise":1711049940,"moonset":1711002900,"moon_phase":0.39,"summary":"The day will start with partly cloudy through the late morning hours, transitioning to rain","temp":{"day":306.07,"min":297.01,"max":306.07,"night":297.32,"eve":302.43,"morn":297.01},"feels_like":{"day":310.47,"night":298.27,"eve":307.77,"morn":297.7},"pressure":1010,"humidity":54,"dew_point":295.39,"wind_speed":2.17,"wind_deg":317,"wind_gust":2.89,"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10d"}],"clouds":100,"pop":0.94,"rain":2.3,"uvi":5},{"dt":1711119600,"sunrise":1711099910,"sunset":1711143417,"moonrise":1711138440,"moonset":1711092240,"moon_phase":0.42,"summary":"There will be rain today","temp":{"day":305.84,"min":296.15,"max":305.84,"night":297.44,"eve":300.11,"morn":296.15},"feels_like":{"day":311.22,"night":298.41,"eve":303.57,"morn":297.04},"pressure":1011,"humidity":58,"dew_point":296.55,"wind_speed":1.79,"wind_deg":13,"wind_gust":2.29,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":98,"pop":1,"rain":12.93,"uvi":5},{"dt":1711206000,"sunrise":1711186315,"sunset":1711229774,"moonrise":1711226940,"moonset":1711181400,"moon_phase":0.45,"summary":"There will be rain today","temp":{"day":297.84,"min":296.07,"max":302.99,"night":296.07,"eve":297.96,"morn":296.43},"feels_like":{"day":298.79,"night":297,"eve":298.95,"morn":297.4},"pressure":1010,"humidity":93,"dew_point":296.71,"wind_speed":1.74,"wind_deg":252,"wind_gust":4.46,"weather":[{"id":501,"main":"Rain","description":"moderate rain","icon":"10d"}],"clouds":100,"pop":1,"rain":29.15,"uvi":5}],"alerts":[{"sender_name":"Instituto Nacional de Meteorologia","event":"Chuvas Intensas","start":1710595860,"end":1710680400,"description":"INMET publica aviso iniciando em: 16/03/2024 10:31. Chuva entre 20 e 30 mm/h ou até 50 mm/dia, ventos intensos (40-60 km/h). Baixo risco de corte de energia elétrica, queda de galhos de árvores, alagamentos e de descargas elétricas.","tags":["Rain"]}]}
it_will_rain = False
for hour in response['hourly'][:12]:  # Just pick the next twelve hours

    ts = hour['dt']
    date = dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    # print(date)
    datetime_obj = dt.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        it_will_rain = True
if it_will_rain:
    send_sms('Bring an umbrella')
