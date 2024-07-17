document.addEventListener("DOMContentLoaded", function() {
    var photo = document.getElementById('animated-photo');
    
    // Add event listener for click event
    photo.addEventListener('click', function() {
      // Toggle bounce and rotate classes
      this.classList.toggle('rotate');
      
      // Remove bounce and rotate classes after animation ends
      setTimeout(() => {
        this.classList.remove('rotate');
      }, 3000); // Adjust this timing to match the animation duration
    });
    
    // Trigger the animations on page load
    photo.classList.add( 'rotate');
  });
  
  document.addEventListener("DOMContentLoaded", function() {
    var navToggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('nav');
    var photo = document.getElementById('animated-photo');
    
    navToggle.addEventListener('click', function() {
        nav.classList.toggle('active');
        navToggle.classList.toggle('active');
        
        // If nav is not active after toggling, hide it
        if (!nav.classList.contains('active')) {
            setTimeout(function() {
                nav.style.display = 'none';
            }, 500); // Adjust the delay as needed to match your CSS transition duration
        } else {
            nav.style.display = 'block'; // Ensure nav is visible when toggled active
        }
    });
    
    photo.addEventListener('click', function() {
        photo.classList.toggle('rotate');
        setTimeout(() => {
            photo.classList.remove('rotate');
        }, 4000);
    });
    
    // Initially rotate the photo
    photo.classList.add('rotate');
  });
  