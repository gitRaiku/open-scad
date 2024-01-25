$fn = 200;

union() {
	translate(v = [5.649999999999999, 8.0, 0]) {
		color(alpha = 1.0, c = [0.8616090647292522, 0.536495730113334, 0.19548899031476086]) {
			square(center = false, size = [90.7, 122.5]);
		}
	}
	linear_extrude(height = 12) {
		translate(v = [5.649999999999999, 8.0, 0]) {
			color(alpha = 1.0, c = [0.8616090647292522, 0.536495730113334, 0.19548899031476086]) {
				square(center = false, size = [90.7, 122.5]);
			}
		}
	}
}
