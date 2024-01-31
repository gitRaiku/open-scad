$fn = 20;

difference() {
	translate(v = [0, 0, -10]) {
		linear_extrude(height = 10) {
			translate(v = [0, -1.4699999999999989, 0]) {
				translate(v = [-10.0, -20.03, 0.0]) {
					color(alpha = 1.0, c = [0.962272393509669, 0.3976451968965351, 0.8008274363432775]) {
						square(center = false, size = [420, 271.06]);
					}
				}
			}
		}
	}
	translate(v = [0, 0, -9]) {
		linear_extrude(height = 9) {
			union() {
				color(alpha = 1.0, c = [0.9677975592919913, 0.44127456009157356, 0.5358103155058701]) {
					square(center = false, size = [400, 231]);
				}
				translate(v = [0, -121.24, 0]) {
					translate(v = [54.75, 109.75, 0.0]) {
						color(alpha = 1.0, c = [0.8616090647292522, 0.536495730113334, 0.19548899031476086]) {
							square(center = false, size = [290.5, 11.5]);
						}
					}
				}
				translate(v = [0, -6, 0]) {
					translate(v = [0, -121.24, 0]) {
						translate(v = [54.75, 109.75, 0.0]) {
							color(alpha = 1.0, c = [0.8616090647292522, 0.536495730113334, 0.19548899031476086]) {
								square(center = false, size = [290.5, 11.5]);
							}
						}
					}
				}
				translate(v = [180.0, 119.77, 0.0]) {
					translate(v = [192.5, 111.22, 0.0]) {
						color(alpha = 1.0, c = [0.21044753832183283, 0.6773105080456748, 0.6433941168468681]) {
							square(center = false, size = [15, 8.56]);
						}
					}
				}
				translate(v = [-180.0, 119.77, 0.0]) {
					translate(v = [192.5, 111.22, 0.0]) {
						color(alpha = 1.0, c = [0.21044753832183283, 0.6773105080456748, 0.6433941168468681]) {
							square(center = false, size = [15, 8.56]);
						}
					}
				}
				translate(v = [180.0, -119.77, 0.0]) {
					translate(v = [192.5, 111.22, 0.0]) {
						color(alpha = 1.0, c = [0.21044753832183283, 0.6773105080456748, 0.6433941168468681]) {
							square(center = false, size = [15, 8.56]);
						}
					}
				}
				translate(v = [-180.0, -119.77, 0.0]) {
					translate(v = [192.5, 111.22, 0.0]) {
						color(alpha = 1.0, c = [0.21044753832183283, 0.6773105080456748, 0.6433941168468681]) {
							square(center = false, size = [15, 8.56]);
						}
					}
				}
			}
		}
	}
}
