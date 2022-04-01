var totalYears;
var startYear;
let endYear;
var difference;
var newCarsBox;
var txtNewInputBox;
var divTag;
var inputOfCars = [];
var index = 0;
var values;
let dataToBeSend;
var names;
var checkedValues;
var namesofcheck;

function createNewElement(event) {
    
    // totalYears=difference;
    startYear = parseInt(document.getElementById('Starting_Year').value);
    endYear = parseInt(document.getElementById('Ending_Year').value);
    console.log("Starting Year is"+startYear);
    console.log("Ending Year is"+endYear);
    if( endYear  <  startYear ) {
        alert("You Have Not Entered Valid Year");
    } else {

    difference = parseInt(endYear) - parseInt(startYear);
    console.log("Total Number of Column is"+difference);
     totalYears = difference;

    for(var i=0;i<=difference;i++) { 
    newCarsBox = document.createElement('input');
    // txtNewInputBox = document.createElement('input');
    divTag = document.createElement('div');
    
    console.log("Total NO Of Years is "+totalYears);
    // For Year
	// txtNewInputBox.innerHTML = " <input type='number' id='newInputBox' >";
    // For Number of cars


    // newCarsBox.innerHTML = " <input type='number'  id=index > "
    $('#data').append('<input type="number"  placeholder=" Enter No Of Vehicle Here "  name="value'+ i +'"    id="carinput'+ i +'" />');
   
    
	// document.getElementById("data").appendChild(txtNewInputBox).placeholder=startYear++;

    // document.getElementById("data").appendChild(newCarsBox).placeholder=" Enter No Of Vehicle Here ";
    
    document.getElementById("data").appendChild(divTag);
    
    }
}

}



function TotalYears() {
    for(var i=0;i<=difference;i++){
        values = 'carinput' + i;
        inputOfCars[i] = parseInt(document.getElementById(values).value);
    }
    for(var j=0;j<i;j++) {
    console.log(inputOfCars[j]);
    }

    


    // const dict_values = { startYear, endYear }
    // const s = JSON.stringify(dict_values);
    // console.log(s);
    // // window.alert(s);

    // $.ajax({
    //     url:"/",
    //     type:"POST",
    //     contentType : "application/json"
    // })

}




// function confirmMaterial() {    
//     var values = [].filter.call(document.getElementsByName('checked_values'), function(c) {
//         return c.checked;
//       }).map(function(c) {
//         return c.value;
//       });
//       document.getElementById('show').innerText = JSON.stringify('You Have Selected'+values).toString();
    
// }




// $("input :checkbox ").attr("checked",false).click(function()
// {
//     var shcolumn="."+$(this).attr("name");
//     $ (shcolumn).toggle();
// }


// function confirmMaterial() {    
//     $("input :checkbox ").attr("checked",false).click(function()
// {
//     var shcolumn="."+$(this).attr("name");
//     $ (shcolumn).toggle();
// })
// }



function hide_show_table(col_name)
{
 var checkbox_val=document.getElementById(col_name).value;
 if(checkbox_val=="hide")
 {
  var all_col=document.getElementsByClassName(col_name);
  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="none";
  }
  document.getElementById(col_name+"_head").style.display="none";
  document.getElementById(col_name).value="show";
 }
	
 else
 {
  var all_col=document.getElementsByClassName(col_name);
  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="table-cell";
  }
  document.getElementById(col_name+"_head").style.display="table-cell";
  document.getElementById(col_name).value="hide";
 }
}