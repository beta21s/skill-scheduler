import os
from LuanVan import app

app.config['SERVER'] = '0.0.0.0'
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9000))
    app.run(app.config['SERVER'], port=port, debug=True)
