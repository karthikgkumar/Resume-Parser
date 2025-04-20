document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('upload-form');
    const resultSection = document.getElementById('result');
    
    if (uploadForm) {
        uploadForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData();
            const fileInput = document.getElementById('resume');
            formData.append('resume', fileInput.files[0]);
            
            try {
                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    displayResults(data.data);
                } else {
                    alert(data.error || 'Error processing resume');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error uploading file');
            }
        });
    }
    
    function displayResults(data) {
        resultSection.style.display = 'block';
        
        // Display basic information
        document.getElementById('name').textContent = data.name || 'N/A';
        document.getElementById('email').textContent = data.email || 'N/A';
        document.getElementById('phone').textContent = data.phone || 'N/A';
        
        // Display skills
        const skillsContainer = document.getElementById('skills');
        skillsContainer.innerHTML = '';
        if (data.skills && data.skills.length > 0) {
            data.skills.forEach(skill => {
                const skillTag = document.createElement('span');
                skillTag.className = 'skill-tag';
                skillTag.textContent = skill;
                skillsContainer.appendChild(skillTag);
            });
        } else {
            skillsContainer.textContent = 'No skills found';
        }
        
        // Display work experience
        const experienceContainer = document.getElementById('experience');
        experienceContainer.innerHTML = '';
        if (data.work_experience && data.work_experience.length > 0) {
            data.work_experience.forEach(exp => {
                const expDiv = document.createElement('div');
                expDiv.className = 'experience-item';
                expDiv.innerHTML = `
                    <h4>${exp.company || 'Unknown Company'}</h4>
                    <p class="dates">${exp.dates || 'Dates not specified'}</p>
                    <p class="description">${exp.description || 'No description available'}</p>
                `;
                experienceContainer.appendChild(expDiv);
            });
        } else {
            experienceContainer.textContent = 'No work experience found';
        }
    }
});
