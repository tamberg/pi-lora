$fn=36;

// box size
w = 77.5;
h = 3;

// pi zero size
pi_wx = 58;//65;
pi_wy = 23;//30;

// pi zero pos
pi_x = 5;
pi_y = 5;

// lora module size
rn_wx = 38;
rn_wx2 = 42.5;
rn_wy = 26.5;

// lora module pos
rn_x = 5;
rn_y = w - rn_wy - 5;

// screw hole size
r_25 = .94;

module base() {
    e=4;
    w2=w-2*e;
    translate([e, e, 0]) hull() {
        translate([0, 0, 0]) cylinder(h, e, e);
        translate([w2, 0, 0]) cylinder(h, e, e);
        translate([0, w2, 0]) cylinder(h, e, e);
        translate([w2, w2, 0]) cylinder(h, e, e);
    }
}

!projection() 
difference() {
    base();
    // pi zero screw holes
    translate([pi_x, pi_y, -1]) cylinder(h + 2, r_25, r_25);
    translate([pi_x + pi_wx, pi_y, -1]) cylinder(h + 2, r_25, r_25);
    translate([pi_x, pi_y + pi_wy, -1]) cylinder(h + 2, r_25, r_25);
    translate([pi_x + pi_wx, pi_y + pi_wy, -1]) cylinder(h + 2, r_25, r_25);
 
    // lora module screw holes
    translate([rn_x, rn_y, -1]) cylinder(h + 2, r_25, r_25);
    translate([rn_x + rn_wx2, rn_y, -1]) cylinder(h + 2, r_25, r_25);
    translate([rn_x, rn_y + rn_wy, -1]) cylinder(h + 2, r_25, r_25);
    translate([rn_x + rn_wx, rn_y + rn_wy, -1]) cylinder(h + 2, r_25, r_25);   

    // lora antenna hole
    translate([w - 26, w - 17, -1]) cube([26, 17, h + 2]);
    translate([w - 15, w - 34, -1]) cube([15, 34, h + 2]);
    translate([w, w - 34, -1]) cylinder(h + 2, 15, 15);

    // finger hole
    translate([2 * w/4, 1 * w/4, -1]) cylinder(h + 2, 10, 10);
}
