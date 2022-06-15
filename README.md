<div align='center'>
    <h1>OculiScraper</h1>
    <small>(plural for Oculus)</small>
</div>

<h3 align='center'>Headless Web Scraper on Oculus titles and descriptions</h3>

<h3 align='center'>GOALS</h3>

* Fetch all necessary URIs from main catalog according to whitelist
* Extract description from game page
* Output to whatever file format I want

Issues faced
------------
* Website contains events and flex

Resolution
------------
* Used Selenium and XPath as a workaround, even though BeautifulSoup might've been an elegant solution.
