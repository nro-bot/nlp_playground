def get_strings() -> list:
    str1A = 'gleason score 3+3 = 6; 3 of 3 cores; 40%'
    str1B = 'gleason score 4+4=9; one of two; 10%'
    str2 = 'gleason 3+4=7/10, involving 5% of 1/2 cores'
    str3 = 'gleason grade 3+4 \n\t (combined gleason score 7/10) involving 2 (of 2) cores'
    str4 = 'gleason scores 6/10) involving '
    str5A = 'gleason score 7 (3+4) in one of one'
    str5B = 'gleason score 9 (4+5) in one of one'
    str5C = 'adenocarcinoma, grade group 2, gleason score 7 (3+4)'
    str_8 = 'gleason pattern 4 is noted'
    str9A = "gleason's score 3+3"
    str9B = "gleason's score 4 + 3"
    str10 = "GLEASON pattern 3+4(10%)=7 (GRADE GROUP 2)."
    return [str1A, str1B, 
            str2, str3, str4,
            str5A, str5B, str5C,
            str_8,
            str9A,
            str9B,
            str10]
