var results = "https://api.github.com/users/octocat/gists"

var Title = React.createClass({
	propTypes: {
		title: React.PropTypes.string
	},

	render: function() {
		return (
			<header><h2>{this.props.title}</h2></header>
			)
	}
})

var SearchResults = React.createClass({
	propTypes: {
		desc: React.PropTypes.string
	},

	getDefaultProps: function() {
		return {
			desc: 'No results from your search input.'
		}
	},

	getInitialState: function() {
		return {
			id: '',
			username: '',
			lastGistUrl: ''
		};
	},

	componentDidMount: function() {
		this.serverRequest = $.get(this.props.results, function (result) {
			console.log(result);
			var i = 0
			var lastGist = result[i];
			this.setState({
				id: lastGist.id,
				username: lastGist.owner.login,
       			lastGistUrl: lastGist.html_url
			});
			i=i+1
		}.bind(this));
	},

	componentWillUnmount: function() {
		this.serverRequest.abort();
	},

	render: function() {
		console.log("this state = " + this.state.results);
		console.log("this props result = " + this.props.results);

		var model = "N/A"
		if (this.props.isModel) {
			model = (<Model desc={this.props.desc} />)
		}

		return (
			<div>
				<ul>
					<li>{this.state.username}<br/>
					{this.state.lastGistUrl}<br/>
					{this.state.id}
					</li>
					<p> {this.state.username}s last gist is <a href={this.state.lastGistUrl}>here</a> with id {this.state.id}. </p>
				</ul>
			</div>
			)
	}
})

var Result = React.createClass({
	propTypes: {
		desc: React.PropTypes.string
	},
	render: function() {
		return (
			<li>
				<p> {this.state.username}s last gist is <a href={this.state.lastGistUrl}>here</a>. </p>
			</li>
		)
	}
})

ReactDOM.render(
	<SearchResults results={results} />,
	document.getElementById('search_results')
);

ReactDOM.render(
	<Title title="Search Results" />,
	document.getElementById('head')
);