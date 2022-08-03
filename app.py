import os
from LuanVan import app
from flask_cors import CORS

app.config['SERVER'] = '0.0.0.0'
if __name__ == '__main__':

    CORS(app)
    cors = CORS(app, resource={
        r"/*": {
            "origins": "*"
        }
    })

    port = int(os.environ.get("PORT", 9000))
    app.run(app.config['SERVER'], port=port, debug=True)
