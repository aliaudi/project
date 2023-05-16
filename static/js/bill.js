
document.addEventListener('keyup',function (){

    let x1=document.getElementById('unit1').value ;
    let y1=document.getElementById('price_unit1').value ;
    let z1=document.getElementById('number_unit1').value ;

    let h1=document.getElementById('allmoney1').value= +y1 * +z1 ;

    let x2=document.getElementById('unit2').value ;
    let y2=document.getElementById('price_unit2').value ;
    let z2=document.getElementById('number_unit2').value ;

    let h2=document.getElementById('allmoney2').value= +y2 * +z2 ;

    let x3=document.getElementById('unit3').value ;
    let y3=document.getElementById('price_unit3').value ;
    let z3=document.getElementById('number_unit3').value ;
    let h3=document.getElementById('allmoney3').value= +y3 * +z3 ;

    let x4=document.getElementById('unit4').value ;
    let y4=document.getElementById('price_unit4').value ;
    let z4=document.getElementById('number_unit4').value ;

    let h4=document.getElementById('allmoney4').value= +y4 * +z4 ;

    // let x5=document.getElementById('unit5').value ;
    // let y5=document.getElementById('price_unit5').value ;
    // let z5=document.getElementById('number_unit5').value ;

    // let h5=document.getElementById('allmoney5').value= +y5 * +z5 ;

    // let x6=document.getElementById('unit6').value ;
    // let y6=document.getElementById('price_unit6').value ;
    // let z6=document.getElementById('number_unit6').value ;

    // let h6=document.getElementById('allmoney6').value= +y6 * +z6 ;

    // let x7=document.getElementById('unit7').value ;
    // let y7=document.getElementById('price_unit7').value ;
    // let z7=document.getElementById('number_unit7').value ;

    // let h7=document.getElementById('allmoney7').value= +y7 * +z7 ;

    // let x8=document.getElementById('unit8').value ;
    // let y8=document.getElementById('price_unit8').value ;
    // let z8=document.getElementById('number_unit8').value ;

    // let h8=document.getElementById('allmoney8').value= +y8 * +z8 ;

    // let x9=document.getElementById('unit9').value ;
    // let y9=document.getElementById('price_unit9').value ;
    // let z9=document.getElementById('number_unit9').value ;

    // let h9=document.getElementById('allmoney9').value= +y9 * +z9 ;

    // let x10=document.getElementById('unit10').value ;
    // let y10=document.getElementById('price_unit10').value ;
    // let z10=document.getElementById('number_unit10').value ;

    // let h10=document.getElementById('allmoney10').value= +y10 * +z10 ;
    let mm=document.getElementById("allvalue_of_bill") ;    
    let cc=document.getElementById("allvalue_of_bill_after_tax") ;
    let g=[h1,h2,h3,h4] ;
    let d = 0 ;
    for( let i=0; i<g.length; i++){
            
            if(g[i] !== "" ){
                  
                d += g[i]
                print(d)
                mm.value= +d ; 
                cc.value= +d + (0.16 * +d)
          
            }
            }
      
     }

);
