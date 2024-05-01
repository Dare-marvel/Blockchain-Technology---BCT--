const HDWalletProvider = require('@truffle/hdwallet-provider');

module.exports = {
  networks: {
    sepolia: {
      provider: () => new HDWalletProvider(
        "drastic taste win among vapor best thrive uncover vibrant index quarter margin",
        "https://sepolia.infura.io/v3/fcb58e5accf94b498717e664cd2a3c2e"
      ),
      network_id: 11155111, // Sepolia's network id
      chain_id: 5, // Sepolia's chain id
      gas: 5500000, // Gas limit used for deploys
      confirmations: 2, // # of confirmations to wait between deployments (default: 0)
      timeoutBlocks: 2000, // # of blocks before a deployment times out (minimum/default: 50)
      skipDryRun: false // Skip dry run before migrations? (default: false for public nets)
    },
  },
  compilers: {
    solc: {
      version: "0.8.21", // Fetch exact version from solc-bin (default: truffle's version)
      settings: { // See the solidity docs for advice about optimization and evmVersion
        optimizer: {
          enabled: false,
          runs: 200
        },
        evmVersion: "byzantium"
      }
    }
  }
};
