//SPDX-License-Identifier: MIT

pragma solidity ^0.8.26;

contract calculator{

    uint256 output=0;

    function division(uint256 n1,uint256 n2) public {

         output = n1/n2;
         
    }
    
   

    function multiplication(uint256 n1,uint256 n2) public {

         
         output = n1*n2;
        
    }

     function addition(uint256 n1,uint256 n2) public {

         
         output = n1+n2;
         
    }

    function subtraction(uint256 n1,uint256 n2) public {

         
         output = n1-n2;
         
    }
    
    function get() public view returns  (uint256) {
         return output; 
    }


}
