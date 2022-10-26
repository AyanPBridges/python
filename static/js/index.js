const serverUrl = "";
const appId = "";
Moralis.start({ serverUrl, appId });
const getInfo = async () => {
  const options = {
    network: document.getElementById("network").value,
    address: document.getElementById("address").value,};
  const nftMetadata = await Moralis.SolanaAPI.nft.getNFTMetadata(options);
  console.log(portfolio);};
document.getElementById("get-portfolio").onclick = getInfo();
