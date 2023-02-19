let stripe_pk = document.querySelector("[name='stripe_pk']").getAttribute('content');
let stripe = Stripe(stripe_pk);

document.querySelector('.buy-button').addEventListener('click', onBuyButtonClicked);

async function onBuyButtonClicked(event){
	let url = event.target.getAttribute('action');
	let response = await fetch(url, {'method': 'GET'});
	let session = await response.json();

	stripe.redirectToCheckout({sessionId: session.id});
}
