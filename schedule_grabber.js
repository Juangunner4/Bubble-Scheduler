// ==UserScript==
// @name           myEMU Schedule Grabber
// @namespace      CDC
// @description    Pull Student/Faculty Schedule from myEMU
// @include        https://my.emu.edu/*
// @grant          none
// ==/UserScript==
// Charles Cooley - 2012-04-24, 2012-08-31 update to account for myEMU page structure variations
//                  2013-01-07 support for results of a course search
//					2013-06-25 updated schedulemaker and avoid leading spaces
//					2013-06-26 added more building names, refactored code

var x = document.getElementById("MAINFORM") //this gets the data from the element called mainform
if (x) { x.removeAttribute("autocomplete") } //removes the attribute of autocomplete

var maker='https://moodle.emu.edu/pluginfile.php/104982/mod_resource/content/30/ScheduleMaker.html?', //setting variable value to the hyperlink

//Not understanding what exactly is going on here
framestart='<iframe id="scheduleMaker" style="border: 4px solid black; padding: 1em 0 0 1em" height="2350px" width="750px" src="' + maker,
frameend='">',  linkstart='<p><a target="_blank" href="' + maker,
linkend='">View schedule grid in a new tab or window for printing or saving.</a></p>'


//What is r t s ?
var pg = 0, r, t, s = "", title, col = { course:-1, name:-1, time:-1, place:-1 } //"col" seems to be making the different type of info included inside of a block

while (!t && pg < 9) {
	if (t = document.getElementById("pg"+pg+"_V_dgCourses")) { // from course search (by person or department)
		title = undefined
		x = document.getElementById("pg"+pg+"_CourseSchedules").nextSibling.nextSibling
	} else if (t = document.getElementById("pg"+pg+"_V_ggCourseList")) { // faculty schedule
		title = document.getElementById("pg"+pg+"_V_lblCrsListFor")
		x = document.getElementById("pg"+pg+"_FacultyCourseControlPortlet").nextSibling.nextSibling
	} else if (t = document.getElementById("pg"+pg+"_StudentSchedule")) {
		title = document.getElementById("pg"+pg+"_V_divHeader"); if (title) title = title.firstChild
		x = document.getElementById("divGroupedGrid")
		t = document.getElementById("pg"+pg+"_V_ggCourses") || true
	} else if (t = document.getElementById("pg"+pg+"_AdviseeRoster")) {
		title = document.getElementById("pg"+pg+"_V_divHeader"); if (title) title = title.firstChild
		x = document.getElementById("divGroupedGrid")
		t = document.getElementById("pg"+pg+"_V_ggCourses") || true
	} else {
		pg++
	}
}
if (t && t.tHead) {
	r = t.tHead.rows[t.tHead.rows.length-1].cells
	for (var i = 0; i < r.length; i++) {
		switch (r[i].textContent) {
			case "Name":
			case "Title": col.name = i; break
			case "Course":
			case "Course Code": col.course = i; break
			case "Meets": col.time = i; break
			case "Room": col.place = i; break
			case "Schedule": col.time = col.place = i; break
		}
	}
	if (col.name<0||col.course<0||col.time<0||col.place<0) return
	r = t.tBodies[0].rows
	for (var i = 0 ; i < r.length; i++) {
		if (r[i].style.display != "none") {
			if (col.time == col.place) line = r[i].cells[col.time].getElementsByTagName("li")
			else line = r[i].cells[col.time].children[0].children
			for (var j = 0; j < line.length; j++) {
				var times =  line[j].textContent.replace(/\s+/g," ").replace(/^\s+/,"").replace(/;.*/,"")
				s += times + r[i].cells[col.course].textContent.replace(/\s+/g," ") 
				times = times.match(/(\d+:\d+).*-\D*(\d+:\d+)/)
				if (times) {
					s += "\n``"
			
					s += ((col.time==col.place)?line:r[i].cells[col.place].children[0].children)[j].textContent.replace(/.*;/,"").replace(/\s*Main Campus,\s*/g," ").replace(/Hartzler Library,/,"LB").replace(/Suter Science Center,/,"SC").replace(/University Commons,/,"UC").replace(/Campus Center,/,"CC").replace(/ \D*$/g,"").replace(/\s+/g," ").replace(/^\s*MAIN/,"").replace(/\s*\/\s*/g," ")

					s += "\\`"
				}
				s += "<b>" + r[i].cells[col.name].textContent.replace(/\s+/g," ") + "</b>"
				if (times) s += "\\" + (j>0?"*":"") +  "``" + times[1] + '-' + times[2]
				s += "\n\n"
			}
		}
	}
	s = escape("\n<title>" + (title ? title.innerHTML : "Schedule") + "</title>\n\n" + s)
	x.innerHTML =  linkstart + s + linkend + framestart + s + frameend
}
