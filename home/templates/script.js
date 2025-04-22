document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('itineraryForm');
    const resultsSection = document.getElementById('results');
    const errorDiv = document.getElementById('error');
    const generateBtn = document.getElementById('generateBtn');
  
    form.addEventListener('submit', async function (e) {
      e.preventDefault();
  
      // Get form values
      const destination = document.getElementById('destination').value;
      const budget = document.getElementById('budget').value;
      const duration = document.getElementById('duration').value;
  
      // Get checked preferences
      const preferenceCheckboxes = document.querySelectorAll('input[name="preferences"]:checked');
      const preferences = Array.from(preferenceCheckboxes).map(cb => cb.value);
  
      // Validate form
      if (!destination || !budget || !duration) {
        showError('Please fill in all required fields');
        return;
      }
  
      if (parseFloat(budget) < 100) {
        showError('Minimum budget is $100');
        return;
      }
  
      // Disable button and show loading
      generateBtn.disabled = true;
      generateBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Generating...';
  
      try {
        // Simulate network delay and generate mock data
        await new Promise(resolve => setTimeout(resolve, 1000));
  
        const totalBudget = parseFloat(budget);
        const numDays = parseInt(duration);
  
        const data = {
          destination,
          budget: totalBudget,
          duration: numDays,
          preferences,
          accommodation: "$" + (totalBudget * 0.4).toFixed(2),
          meals: "$" + (totalBudget * 0.2).toFixed(2),
          costBreakdown: [
            { label: "Flights", cost: "$" + (totalBudget * 0.25).toFixed(2) },
            { label: "Accommodation", cost: "$" + (totalBudget * 0.4).toFixed(2) },
            { label: "Meals", cost: "$" + (totalBudget * 0.2).toFixed(2) },
            { label: "Activities", cost: "$" + (totalBudget * 0.1).toFixed(2) },
            { label: "Miscellaneous", cost: "$" + (totalBudget * 0.05).toFixed(2) }
          ],
          dailyItinerary: Array.from({ length: numDays }, (_, i) =>
            `Day ${i + 1}: Enjoy ${preferences.length ? preferences.join(', ') : 'local attractions'} in ${destination}`
          ),
          travelTips: [
            "Book in advance to save money.",
            "Check local events for cultural experiences.",
            "Use public transportation for cost-effective travel."
          ]
        };
  
        displayResults(data);
        errorDiv.style.display = 'none';
  
      } catch (error) {
        console.error('Error:', error);
        showError('An error occurred while generating the itinerary.');
      } finally {
        // Re-enable button
        generateBtn.disabled = false;
        generateBtn.innerHTML = '<i class="fas fa-map-marked-alt"></i> Generate Itinerary';
      }
    });
  
    function showError(message) {
      errorDiv.textContent = message;
      errorDiv.style.display = 'block';
      resultsSection.style.display = 'none';
  
      setTimeout(() => {
        errorDiv.style.display = 'none';
      }, 5000);
    }
  
    function displayResults(data) {
      document.getElementById('tripTitle').textContent = `Trip to ${data.destination}`;
      document.getElementById('budgetSummary').textContent = `Total Budget: $${data.budget} for ${data.duration} days`;
      document.getElementById('accommodation').textContent = data.accommodation;
      document.getElementById('meals').textContent = data.meals;
  
      const breakdownList = document.getElementById('costBreakdown');
      breakdownList.innerHTML = '';
      data.costBreakdown.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.label}: ${item.cost}`;
        breakdownList.appendChild(li);
      });
  
      const dailyDiv = document.getElementById('dailyItinerary');
      dailyDiv.innerHTML = '';
      data.dailyItinerary.forEach(day => {
        const p = document.createElement('p');
        p.textContent = day;
        dailyDiv.appendChild(p);
      });
  
      const tipsList = document.getElementById('travelTips');
      tipsList.innerHTML = '';
      data.travelTips.forEach(tip => {
        const li = document.createElement('li');
        li.textContent = tip;
        tipsList.appendChild(li);
      });
  
      resultsSection.style.display = 'block';
    }
  });