document.addEventListener("DOMContentLoaded", () => {
    const userTypeInput = document.getElementById("id_user_type");
    const donorButton = document.getElementById("donorButton");
    const donorLabel = document.getElementById("donorLabel");
    const donorText = document.getElementById("donorText");
    const recipientButton = document.getElementById("recipientButton");
    const recipientLabel = document.getElementById("recipientLabel");
    const recipientText = document.getElementById("recipientText");


    donorButton.addEventListener('click', () => {
        userTypeInput.value = "donor";
        
        donorButton.classList.remove('border-gray-300', 'hover:border-gray-400', 'bg-gray-50')
        donorButton.classList.add('border-red-600', 'bg-red-50');
        donorLabel.classList.replace('text-gray-700', 'text-red-600');
        donorText.classList.replace("text-gray-500", "text-red-700");
        document.querySelector("#donorButton .lucide-droplet").classList.replace('text-gray-400', 'text-red-600');
        
        
        recipientButton.classList.add('border-gray-300', 'hover:border-gray-400', 'bg-gray-50')
        recipientButton.classList.remove('border-red-600', 'bg-red-50');
        recipientLabel.classList.replace('text-red-600', 'text-gray-700');
        recipientText.classList.replace("text-red-700", "text-gray-500");
        document.querySelector("#recipientButton .lucide-user").classList.replace('text-red-600', 'text-gray-400');
    });
    
    recipientButton.addEventListener('click', () => {
        userTypeInput.value = "recipient";
        
        recipientButton.classList.remove('border-gray-300', 'hover:border-gray-400', 'bg-gray-50')
        recipientButton.classList.add('border-red-600', 'bg-red-50');
        recipientLabel.classList.replace('text-gray-700', 'text-red-600');
        recipientText.classList.replace("text-gray-500", "text-red-700");
        document.querySelector("#recipientButton .lucide-user").classList.replace('text-gray-400', 'text-red-600');
        
        donorButton.classList.add('border-gray-300', 'hover:border-gray-400', 'bg-gray-50')
        donorButton.classList.remove('border-red-600', 'bg-red-50');
        donorLabel.classList.replace('text-red-600', 'text-gray-700');
        donorText.classList.replace("text-red-700", "text-gray-500");
        document.querySelector("#donorButton .lucide-droplet").classList.replace('text-red-600', 'text-gray-400');
    });
});