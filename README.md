# Python Scripts

This is a small repositery that contains different python scripts that i use to ease my daily tasks.

# Contents

- [Project init](https://github.com/chemsedd/python-scripts/tree/master/project-init)
- [Weather API](https://github.com/chemsedd/python-scripts/tree/master/weather-api)

### Project init
A small command line tool that automates the creation of folders. I use it specifically for initializing a design project (Adobe illustrator or Adobe Photoshop).
#### Example:
```bash
python init_dir.py --path my_project -a -j -p
```
![Project init script](screenshots/project-init.jpg)


### Weather API
A command line tool for retrieving weather data from the api.openweathermap.org server. The website provides current detailed weather data about a long list of cities around the world. The command line offers easy retrieval of these data.

```bash
python get-weather.py london --verbose
```