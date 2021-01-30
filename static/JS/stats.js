// var trace1 = {
//     x: [1, 2, 3, 4],
//     y: [10, 15, 13, 17],
//     type: 'scatter' 
// };
// var data1 = [trace1];
// var layout1 = {
//     shapes: [
//     {
//         type: 'line',
//         xref: 'paper',
//         x0: 0,
//         y0: 12.0,
//         x1: 1,
//         y1: 12.0,
//         line:{
//             color: 'rgb(255, 0, 0)',
//             width: 2,
//             dash:'dash'
//         }
//     }
//     ],
//     title: "Sampled Results", 
//     xaxis: {title: "Value"}, 
//     yaxis: {title: "Count"},
//     height: 498,
//     width: 889
// }
// let config1 = { 
//     responsive: true,
//     displaylogo: false,
// };
// Plotly.newPlot('myDiv1', data1, layout1, config1);

// var data2 = [{
//     type: "pie",
//     values: [2, 3],
//     labels: ["Correct Position", "Incorrect Position"],
//     textinfo: "label+percent",
//     insidetextorientation: "radial"
//   }]
  
//   var layout2 = {
//     title: "Sleeping Position of the Baby",
//     height: 498,
//     width: 582
//   }
//   let config2 = { 
//     responsive: true,
//     displaylogo: false,
// };
// Plotly.newPlot('myDiv2', data2, layout2, config2);

// var data3 = [
// 	{
// 		domain: { x: [0, 1], y: [0, 1] },
// 		value: 270,
// 		title: { text: "Temperature" },
// 		type: "indicator",
// 		mode: "gauge+number"
// 	}
// ];

// var layout3 = { width: 582, height: 498, margin: { t: 0, b: 0 } };
// let config3 = { 
//     responsive: true,
//     displaylogo: false,
// };
// Plotly.newPlot('myDiv3', data3, layout3, config3);

// trace4 = {
//     type: 'scatter',
//     x: [1, 2, 3, 4],
//     y: [10, 15, 13, 17],
//     mode: 'lines',
//     name: 'Red',
//     line: {
//       color: 'rgb(219, 64, 82)',
//       width: 3
//     }
//   };
 
//   var layout4 = {
//     title: 'Quarter 1 Growth',
//     xaxis: {
//         title: 'GDP per Capita',
//         showgrid: false,
//         zeroline: false
//     },
//     yaxis: {
//         title: 'Percent',
//         showline: false
//     },
//     height: 498,
//     width: 889
//   };
  
//   var data4 = [trace4];
//   let config4 = { 
//     responsive: true,
//     displaylogo: false,
// };
// Plotly.newPlot('myDiv4', data4, layout4, config4);


function pieupdate(){
  $.post('/pie', {}, (data, error)=>{
    var data2 = [{
        type: "pie",
        values: [100-data, data],
        labels: ["Correct Position", "Incorrect Position"],
        textinfo: "label+percent",
        insidetextorientation: "radial"
      }]
      
      var layout2 = {
        title: "Sleeping Position of the Baby (Today)",
        // height: 498,
        // width: 582
      }
      let config2 = { 
        responsive: true,
        displaylogo: false,
    };
    Plotly.newPlot('myDiv2', data2, layout2, config2);
  });
}

function lnfupdate(){
  $.post('/lnf', {}, (data, error)=>{
    var trace1 = {
        x: data.dates,
        y: data.val,
        type: 'scatter' 
    };
    var data1 = [trace1];
    var layout1 = {
        shapes: [
        {
            type: 'line',
            xref: 'paper',
            x0: 0,
            y0: 15.0,
            x1: 1,
            y1: 15.0,
            line:{
                color: 'rgb(255, 0, 0)',
                width: 2,
                dash:'dash'
            }
        }
        ],
        title: "Daily Wrong Position Percentage", 
        xaxis: {title: "Date"}, 
        yaxis: {title: "Percentage"},
        // height: 498,
        // width: 889
    }
    let config1 = { 
        responsive: true,
        displaylogo: false,
    };
    Plotly.newPlot('myDiv1', data1, layout1, config1);
  });
}
function gtempupdate(){
  $.post('/gtemp', {}, (data, error)=>{
    var data3 = [
      {
        domain: { x: [0, 1], y: [0, 1] },
        value: data,
        title: { text: "Latest Temperature Reading" },
        type: "indicator",
        mode: "gauge+number"
      }
    ];
    
    var layout3 = { 
      // width: 582, 
      // height: 498, 
      margin: { 
        t: 0, 
        b: 0 
      } 
    };
    let config3 = { 
        responsive: true,
        displaylogo: false,
    };
    Plotly.newPlot('myDiv3', data3, layout3, config3);
  });
}

function ltempupdate(){
  $.post('/ltemp', {}, (data, error)=>{
    trace4 = {
      type: 'scatter',
      x: data.x,
      y: data.y,
      mode: 'lines',
      name: 'Red',
      line: {
        color: 'rgb(219, 64, 82)',
        width: 3
      }
    };
   
    var layout4 = {
      title: "Baby's temperature monitor",
      xaxis: {
          title: "Date - Time",
          showgrid: false,
          zeroline: false
      },
      yaxis: {
          title: 'Temperature in Fahrenheit',
          showline: false
      },
      // height: 498,
      // width: 889
    };
    
    var data4 = [trace4];
    let config4 = { 
      responsive: true,
      displaylogo: false,
  };
  Plotly.newPlot('myDiv4', data4, layout4, config4);
  });
}
allup=()=>{
  pieupdate();
  lnfupdate();
  ltempupdate();
  gtempupdate();
};

setInterval(allup, 3000);