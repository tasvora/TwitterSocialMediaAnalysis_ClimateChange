// Select the button
var button = d3.select("#predict-btn");

button.on("click", function () {

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#inputTweet");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");
  if(inputValue != ""){
    getPrediction(inputValue);
    
    
  }else {
    console.log("No value entered")
  }
  console.log(this)
  // Set the span tag in the h1 element to the text
  // that was entered in the form
  // d3.select("h1>span").text(inputValue);
});

function getPrediction(TweetText) {
  var url = "/predictTweet/"+TweetText;
  console.log(url);
  d3.json(url).then(function(response) {
    console.log(response);
      result = "Predicted " + response[0] + ", with a  "+ response[1] + " sentiment.";
      d3.select("#outputPredict").text(result);
      // d3.select("#TweetText").text("");
      
  });
}