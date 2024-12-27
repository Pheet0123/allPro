
  const incrementButton = document.getElementById('click');
  const resetButton = document.getElementById('return');
  const numberDisplay = document.getElementById('number');
  let number = 0;

  incrementButton.addEventListener('click', () => {
   
      number += 1;
        
      numberDisplay.textContent = number;
      
  });

  resetButton.addEventListener('click', () => {
     
      number = 0;

      numberDisplay.textContent = number;
  });