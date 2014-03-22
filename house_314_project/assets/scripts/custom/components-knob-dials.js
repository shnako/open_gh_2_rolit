var ComponentsKnobDials = function () {

    return {
        //main function to initiate the module
        
        init: function () {
            //knob does not support ie8 so skip it
            if (!jQuery().knob || App.isIE8()) {
                return;
            }

            // general knob
            var beingUpdated = false;
            var url = "/controls/set_light_bulb_intensity";
            $(".knob").knob({
                'dynamicDraw': true,
                'thickness': 0.2,
                'tickColorizeValues': true,
                'skin': 'tron',
                'change': function() {
                    if (beingUpdated == false) {
                        beingUpdated = true;
                        //console.log(this.cv);
                        $.post(url, {
                            'BULB_ID': "1",
                            'INTENSITY': this.cv
                        }).success(function() {
                            console.log("Bulb intensity has been updated!");
                        }).fail(function() {
                            console.log("Failed to update the intensity!");
                        });
                    }
                }
            });

            // Don't allow sending many requests
            setInterval(function() {
                beingUpdated = false;
            }, 300);
        }

    };

}();
