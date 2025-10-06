# NASA Space Apps Challenge 2025
NASA Space Apps Challenge 2025 project developed by [Zenith 2024](https://www.zenithpathways.ca/zenith-fellowship-class-of-2024) and [Zenith 2025](https://www.zenithpathways.ca/class-of-2025) fellows.

⭐ [Live WebApp Prototype](https://sharkonauts.netlify.app)

⭐ [Project Submission](https://www.spaceappschallenge.org/2025/find-a-team/coding-the-cosmos/?tab=project)

## Description
The Sharkonauts Initiative is an interactive webapp and accompanying shark tag prototype designed to predict shark movement patterns and habitat suitability in response to climate change. The project was submitted under the challenge titled **Sharks from Space**; objectives can be found on the [NASA Space Apps 2025 Challenge Home Page.](https://www.spaceappschallenge.org/2025/challenges/sharks-from-space/). The entire project was developed in less than 36 hours in-person at the Centennial College Downsview Campus for Aerospace and Innovation.

Due to climate change, shark foraging patterns are shifting rapidly. As key contributors to ocean ecosystems, sharks play an essential role in maintaining marine balance, but research on them remains limited due to sparse data and unpredictable behaviour. The Sharkonauts Initiative seeks to address this by predicting shark movement patterns through existing behavioural data combined with a novel shark tag prototype.

A core component of our project is the Habitability Map, which integrates open-access NASA oceanographic data with known physiological parameters of sharks to predict regions most suitable for their survival. The model generates a global grid of probabilities, visualizing how favourable different ocean areas are for sharks.

We have also developed a working prototype of a shark tag equipped with GPS, a temperature sensor, and a camera. Because shark tag data availability varies widely by species and region, this device can complement our habitability model by tracking understudied populations. To present these findings, we built an interactive web app displaying both the habitability map and a sample tag tracker.

Together, these tools can help scientists and students better predict shark movements and understand their changing habitats in a warming world.


## Tools and Technical Components

All individual code integrated into the webapp can be found in the `src/` directory.
Additional code used to develop the functional hardware prototype can be found in the `Hardware Prototype/` directory.
- **Web Development**: Svelte, JavaScript, HTML, CSS
- **Mathematical Modelling**: Python, Pandas, GeoJson Format
- **Physical Prototype**: ESP32-S3, GPS Module, Temperature Sensor, Camera Module, 3D Printed Housing

## Acknowledgement
The Sharkonauts Initiative team would like to thank the organizers, volunteers, sponsors, and industry mentors of NASA Space Apps Toronto for fostering a welcoming community and providing us with the chance to participate in an invaluable weekend of hands-on activity.