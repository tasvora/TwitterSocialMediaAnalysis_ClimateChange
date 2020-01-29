//Tableau Embed function
function initViz() {
    var containerDiv = document.getElementById("vizContainer"),
    url = "https://public.tableau.com/views/TwitterAnalysis_ClimateProject/Dashboard1?:display_count=y&:origin=viz_share_link";

    var viz = new tableau.Viz(containerDiv, url);
}


function initViz1() {
    var containerDiv = document.getElementById("vizContainer"),
    url = "https://public.tableau.com/views/TwitterData_TextAnalytics_ClimateChange/ClimateStrikeDashboard?:display_count=y&:origin=viz_share_link",
        options = {
            hideTabs: true,
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz = new tableau.Viz(containerDiv, url, options);
    // Create a viz object and embed it in the container div.
}