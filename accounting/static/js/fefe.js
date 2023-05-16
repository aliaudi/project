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
    let mm=document.getElementById("allvalue_of_bill") ;    
    let cc=document.getElementById("allvalue_of_bill_after_tax") ;
    let g=[h1,h2,h3,h4] ;
    let d = 0 ;
    for( let i=0; i<g.length; i++){
            
            if(g[i] !== "" ){
                  
                d += g[i]
               console.log(d)
                mm.value= +d ; 
                cc.value= +d + (0.16 * +d)
          
            }
            }
      
     }

);
