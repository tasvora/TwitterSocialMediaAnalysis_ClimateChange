/* data route */
var url = "/initTwitterdata";
var tbody = d3.select("#tweetsList");

function buildhtml() {
  d3.json(url).then(function(response) {
      d3.select("tbody")
      .selectAll("tr")
      .data(response)
      .enter()
      .append("tr")
      .html(function(d) {
        return `<td>${d.text}</td><td>${d.date}</td><td>${d.search_hashtags}</td>`;
      });
  });
}

buildhtml();
