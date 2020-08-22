{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (scrape_mars.py, line 197)",
     "output_type": "error",
     "traceback": [
      "Traceback \u001b[1;36m(most recent call last)\u001b[0m:\n",
      "  File \u001b[0;32m\"C:\\Users\\marti\\anaconda3\\envs\\PythonData\\lib\\site-packages\\IPython\\core\\interactiveshell.py\"\u001b[0m, line \u001b[0;32m3331\u001b[0m, in \u001b[0;35mrun_code\u001b[0m\n    exec(code_obj, self.user_global_ns, self.user_ns)\n",
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-4-85833ce622f7>\"\u001b[1;36m, line \u001b[1;32m4\u001b[1;36m, in \u001b[1;35m<module>\u001b[1;36m\u001b[0m\n\u001b[1;33m    import scrape_mars\u001b[0m\n",
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\marti\\homework\\web-scraping-challenge\\Missions_to_Mars\\scrape_mars.py\"\u001b[1;36m, line \u001b[1;32m197\u001b[0m\n\u001b[1;33m    mars_data = {\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "# Import Dependencies \n",
    "from flask import Flask, render_template, redirect \n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create an instance of Flask app\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use PyMongo to establish Mongo connection\n",
    "mongo = PyMongo(app, uri=\"mongodb://localhost:27017/mars_app\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def home():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find data\n",
    "mars_info = mongo.db.mars_info.find_one()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Return template and data\n",
    "return render_template(\"index.html\", mars_info=mars_info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Route that will trigger scrape function\n",
    "@app.route(\"/scrape\")\n",
    "def scrape(): "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run scrapped functions\n",
    "mars_info = mongo.db.mars_info\n",
    "mars_data = scrape_mars.scrape_mars_news()\n",
    "mars_data = scrape_mars.scrape_mars_image()\n",
    "mars_f = scrape_mars.scrape_mars_facts()\n",
    "mars_w = scrape_mars.scrape_mars_weather()\n",
    "mars_data = scrape_mars.scrape_mars_hemispheres()\n",
    "mars_info.update({}, mars_data, upsert=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Redirect back to home page\n",
    "return redirect(\"/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\": \n",
    "    app.run(debug= True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
