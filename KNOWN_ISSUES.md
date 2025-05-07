# Python Stream Doeck Library :: KNOWN ISSUES

* Mirabox 293 e 293S devices don't send `Key Down`/`Key Up` events. They support only a generic "key pressed" event.
	+ They are simulated via software.
* Some Mirabox devices support a "Secondary Image" feature, and so it was scaffolded into the `StreamDeck` abstract class
	+ They are essentially image buttons, but without the button.
* Mirabox 293 is untested.
    + I don't have the hardware!
* Mirabox N3 & N4 are not uploading the button images.
	+ Expected to be fixed Soon™.
