
#Welcome Message 
print("-----------------Bienvenido al sistema OAK-----------------");

#System Explication 
print("\n")
print("""

Funcionamiento del sistema:

Oak es un sistema que permite variar el tamaño de las imágenes \n 
rescatando su largo y su ancho de una manera perfecta.
""");

print("Explicación")

print("""

Los datos obtenidos del largo y el ancho de la imágen original son divididos \n
entre diez, después de dicha división el resultado que se obtiene se le resta \n 
al largo y el ancho original, este proceso de resta se repite diez veces, ya que con esto \n 
se obtendrán diez unidades para dicha imagen. \n 

Una vez obtenidas las diez unidades el sistema agarrará la novena y la dividirá entre cuatro, \n 
haciendo este proceso el sistema le brindará la posibilidad de elejir entre otras tres unidades \n 
sabiendo que, la unidad diez y la unidad cuatro son equivalentes a cero. 

""")
get_original_height = input("Escriba el largo original de la imagen: ")
get_original_width  = input("Escriba el ancho original de la imagen: ")
def oak_principal_function():
    print("Usted entró a la función principal");
    print("El largo de su imagen es de: {0:d} píxeles".format(int(get_original_height)));
    print("El ancho de su imagen es de: {0:d} píxeles".format(int(get_original_width)))
    print("A continuación, se le mostrarán las unidades disponibles para la imagen original ")
    #Height Calc 
    get_img_height_toInt = int(get_original_height);
    div_img_height_toInt = get_img_height_toInt / 10; #Divide img height = 10 
    one_subtraction_value = get_img_height_toInt - div_img_height_toInt;
    two_subtraction_value = one_subtraction_value - div_img_height_toInt;
    three_subtraction_value = two_subtraction_value - div_img_height_toInt;
    four_subtraction_value = three_subtraction_value - div_img_height_toInt;
    five_subtraction_value = four_subtraction_value - div_img_height_toInt;
    six_subtraction_value = five_subtraction_value - div_img_height_toInt;
    seven_subtraction_value = six_subtraction_value - div_img_height_toInt;
    eight_subtraction_value = seven_subtraction_value - div_img_height_toInt;
    nine_subtraction_value = eight_subtraction_value - div_img_height_toInt;
    #Nine Units
    super_div_nine_subtraction_value = nine_subtraction_value / 4; #Divide img nine_subtraction_value = 4
    #Same process 
    especial_first_value = nine_subtraction_value - super_div_nine_subtraction_value;
    especial_second_value = especial_first_value - super_div_nine_subtraction_value;
    especial_third_value = especial_second_value - super_div_nine_subtraction_value;
    #Three special units
    #Width Calculation
    get_img_width_toInt = int(get_original_width);
    div_img_width_toInt = get_img_width_toInt / 10;
    one_subtraction_w_value = get_img_width_toInt - div_img_width_toInt;
    two_subtraction_w_value = one_subtraction_w_value - div_img_width_toInt;
    three_subtraction_w_value = two_subtraction_w_value - div_img_width_toInt;
    four_subtraction_w_value = three_subtraction_w_value - div_img_width_toInt;
    five_subtraction_w_value = four_subtraction_w_value - div_img_width_toInt;
    six_subtraction_w_value = five_subtraction_w_value - div_img_width_toInt;
    seven_subtraction_w_value = six_subtraction_w_value - div_img_width_toInt;
    eight_subtraction_w_value = seven_subtraction_w_value - div_img_width_toInt;
    nine_subtraction_w_value = eight_subtraction_w_value - div_img_width_toInt;
    super_div_nine_w_subtraction_value = nine_subtraction_w_value / 4; #Divide img nine_subtraction_w_value = 4 
    #Same process
    especial_first_w_value = nine_subtraction_w_value - super_div_nine_w_subtraction_value;
    especial_second_w_value = especial_first_w_value - super_div_nine_w_subtraction_value;
    especial_third_w_value = especial_second_w_value - super_div_nine_w_subtraction_value;
    print("Las unidades básicas son: ") #Basic Units 
    
    #Print Values 

    print(str(one_subtraction_value) + " x " + str(one_subtraction_w_value) +     "             GIGAGIGAGIGA")
    print(str(two_subtraction_value) + " x " + str(two_subtraction_w_value) +     "                 GIGAGIGA")
    print(str(three_subtraction_value) + " x " + str(three_subtraction_w_value) + "                     GIGA")
    print(str(four_subtraction_value) + " x " + str(four_subtraction_w_value) +   "                BIGBIGBIG")
    print(str(five_subtraction_value) + " x " + str(five_subtraction_w_value) +   "                   BIGBIG")
    print(str(six_subtraction_value) +  " x " + str(six_subtraction_w_value)   +  "                      BIG")
    print(str(seven_subtraction_value) + " x " + str(seven_subtraction_w_value) + "       MEDIUMMEDIUMMEDIUM")
    print(str(eight_subtraction_value) + " x " + str(eight_subtraction_w_value) + "             MEDIUMMEDIUM")
    print(str(nine_subtraction_value) +  " x " + str(nine_subtraction_w_value) +  "                   MEDIUM")

    print("Las unidades especiales son: ") #Special Units

    #Special Print Values 
    print(str(especial_first_value) + " x " + str(especial_first_w_value) +   "             SMALLSMALLSMALL")
    print(str(especial_second_value) + " x " + str(especial_second_w_value) + "                  SMALLSMALL")
    print(str(especial_third_value) + " x " + str(especial_third_w_value) +   "                       SMALL")
oak_principal_function();

    
    
    


