// just notes does not compile

// we are going to look at this code and break it down 
template <typename T>
typename std::enable_if<!core::is_duration<T>::value, T>::type
    getIfExists(const nlohmann::json& j, const std::string& key, T&& default_value) {
  return j.contains(key) && !j.at(key).is_null() ? j.at(key).get<T>() : default_value;
}

// first
typename std::enable_if<!core::is_duration<T>::value, T>::type
// enable_if will takes in a condition <condition, type>
// if the condition is true we will assign type T to as the return type for 
// the function below 


// second
getIfExists(const nlohmann::json& j, const std::string& key, T&& default_value) {
  return j.contains(key) && !j.at(key).is_null() ? j.at(key).get<T>() : default_value;
}
// we take in a nlohmann type which is a 3rd party json parsing lib
// T&& is a r value reference, T& would be a l value reference 
