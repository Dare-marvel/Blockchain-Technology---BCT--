// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract UniqueAsset is ERC721URIStorage {
    uint private _tokenIds;

    constructor() ERC721("UniqueAsset", "UNA") {}

    function awardItem(address recipient, string memory metadata) public returns (uint256) {
        uint256 newItemId = _tokenIds;
        _mint(recipient, newItemId);
        _tokenIds += 1;
        _setTokenURI(newItemId, metadata);
        return newItemId;
    }
}

