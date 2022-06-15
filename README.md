<div align='center'>
    <h1>OculiScraper</h1>
    <small>(plural for Oculus)</small>
</div>

<h2 align='center'>Headless Web Scraper on Oculus titles and descriptions</h2>

<body align='center'>
    <h2>GOALS</h2>
    <ul>
      <li>Fetch all necessary URIs from main catalog according to whitelist  </li>
      <li>Extract description from game page</li>
      <li>Output to whatever file format I want</li>
    </ul> 
</body>

<h2 align='center'>Issues faced</h2>

* Website contains events and flex

<h2 align='center'>Resolution</h2>

* Used Selenium and XPath as a workaround, even though BeautifulSoup might've been an elegant solution.
