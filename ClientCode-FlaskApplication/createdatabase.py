from app import db
db.create_all()
from app import Camera #,Traffic
camera1_to_add=Camera(id=1, location='Great Britain M6 highway,going South', road_length=0.19611742)
camera2_to_add=Camera(id=2, location='Great Britain M6 highway,going North', road_length=0.19611742)
camera3_to_add=Camera(id=3, location='Vinhomes smart city', road_length=0.089)

db.session.add(camera1_to_add)
db.session.add(camera2_to_add)
db.session.add(camera3_to_add)

db.session.commit()
Camera.query.all()