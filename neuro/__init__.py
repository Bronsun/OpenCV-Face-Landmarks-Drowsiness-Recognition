from flask import Flask




app = Flask(__name__)
app.secret_key = 'ashdfhjfsge2221qjsajkd1'





from neuro.Main.routes import Main
from neuro.Thermal.routes import Thermal
from neuro.Haar.routes import Haar
from neuro.Hog.routes import Hog
from neuro.Drowsiness.routes import Drowsiness
from neuro.Dlib.routes import Dlib
from neuro.Contact.routes import Contact
from neuro.ThermalDrowsiness.routes import ThermalDrowsiness
from neuro.RGB.routes import RGB
from neuro.DlibRGB.routes import DlibRGB
from neuro.RGBDrowsiness.routes import RGBDrowsiness
from neuro.Photo.routes import Photo

app.register_blueprint(Photo)
app.register_blueprint(RGBDrowsiness)
app.register_blueprint(DlibRGB)
app.register_blueprint(RGB)
app.register_blueprint(ThermalDrowsiness)
app.register_blueprint(Contact)
app.register_blueprint(Dlib)
app.register_blueprint(Drowsiness)
app.register_blueprint(Hog)
app.register_blueprint(Haar)
app.register_blueprint(Main)
app.register_blueprint(Thermal)
